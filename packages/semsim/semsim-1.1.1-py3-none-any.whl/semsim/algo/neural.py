'''Graph neural network implementation.'''

from typing import Any, Callable

import numpy as np
import torch
from torch import nn, Tensor
from torch.nn import functional as fn
from torch.optim import Optimizer
from torch_geometric.data import Data
from torch_geometric.loader import DataLoader
import torch_geometric.nn as pyg_nn
from tqdm import tqdm

from ..exception import ArgumentError
from .tag import DEPREL_TO_IDX
from .tree import Node, Tree


__all__ = (
    'GAT',
    'GCN',
    'build_pyg_dataset',
    'get_edge_ohe',
    'train_gnn',
)


DataBatch = Any
LRScheduler = Any


def get_edge_ohe(child: Node) -> Tensor:
    '''
    Get one-hot encoded vector for an edge from the current node to its parent.

    :param child: dependant node of a relation
    :return: one-hot encoded torch.Tensor for a type of dependency relation
    '''

    n_deps = len(DEPREL_TO_IDX)
    attr = torch.zeros(n_deps - 1)
    idx = DEPREL_TO_IDX[child.deprel]
    if idx < n_deps - 1:
        attr[idx] = 1
    return attr


def build_pyg_dataset(
    tree_pairs: list[tuple[Tree, Tree]],
    labels: list[int] | None = None,
    get_edge_attr: Callable[[Node], Tensor] = get_edge_ohe,
) -> list[Data]:
    '''
    Get list of torch_geometric.data.Data instances from a list of tree pairs.

    :param tree_pairs: list of tree pairs composing a dataset
    :param labels: list of labels for tree pairs
    :param get_edge_attr: callback for obtaining edge attribute vectors
    :return: list of torch_geometric.data.Data instances
    '''

    dataset = []

    for i, (lhs, rhs) in enumerate(tree_pairs):
        if any(node.embedding is None for tree in (lhs, rhs) for node in tree):
            raise ArgumentError(
                'All tree nodes should have an embedding '
                'to build a dataset for graph NN model.'
            )

        x = torch.cat(
            [node.embedding.reshape(1, -1) for node in lhs] +  # type: ignore
            [node.embedding.reshape(1, -1) for node in rhs],   # type: ignore
            dim=0,
        )

        shift = lhs.size
        edge_index = []
        edge_attr = []
        for node in lhs:
            for child in node.children:
                edge_index.append((node.idx - 1, child.idx - 1))
                attr = get_edge_attr(child)
                edge_attr.append(attr.reshape(1, -1))
        for node in rhs:
            for child in node.children:
                edge_index.append((shift + node.idx - 1, shift + child.idx - 1))
                attr = get_edge_attr(child)
                edge_attr.append(attr.reshape(1, -1))

        edge_attr_tensor = (
            torch.cat(edge_attr, dim=0)
            if edge_attr
            else torch.tensor([], dtype=float)  # type: ignore
        )

        data = Data(
            x=x,
            edge_index=torch.tensor(edge_index, dtype=int).T.contiguous(),  # type: ignore
            edge_attr=edge_attr_tensor,
            y=labels[i] if labels is not None else None,
        )
        dataset.append(data)

    return dataset


class GCN(nn.Module):
    '''Graph convolutional binary classification network implementation.'''

    def __init__(
        self,
        *,
        input_dim: int = 300,
        hidden_dim: int = 64,
        num_layers: int = 1,
        dropout: float = 0,
        edge_dim: int | None = None,
    ):
        '''
        GCN initialization.

        :param input_dim: dimensionality of an input vector
        :param hidden_dim: dimensionality of vectors in hidden layers
        :param num_layers: number of hidden convolutional layers
        :param dropout: dropout rate
        :param edge_dim: dimensionality of edge attribute vectors
        '''

        super().__init__()

        self.dropout = dropout

        self.convs = nn.ModuleList()
        for i in range(num_layers):
            in_dim = hidden_dim if i else input_dim
            self.convs.append(pyg_nn.Sequential('x, edge_index', [
                (pyg_nn.convs.GCNConv(
                    in_dim,
                    hidden_dim,
                    concat=False,
                    edge_dim=edge_dim,
                ), 'x, edge_index -> x'),
                pyg_nn.norm.GraphNorm(in_channels=hidden_dim),
                nn.PReLU(num_parameters=hidden_dim),
            ]))

        self.post_mp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Dropout(dropout),
            nn.PReLU(num_parameters=hidden_dim),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid(),
        )

    def forward(self, data: DataBatch) -> Tensor:
        '''
        Apply a forward pass for a data batch.

        :param data: torch_geometric.data.batch.DataBatch instance to process
        :return: torch.Tensor with class probabilities for each data instance in a batch
        '''

        x, edge_index, batch = data.x, data.edge_index, data.batch

        for conv in self.convs:
            x = conv(x, edge_index)
        x = pyg_nn.global_max_pool(x, batch)
        x = self.post_mp(x)

        return x


class GAT(nn.Module):
    '''Graph attention binary classification network implementation.'''

    def __init__(
        self,
        *,
        input_dim: int = 300,
        hidden_dim: int = 64,
        num_heads: int = 1,
        num_layers: int = 1,
        dropout: float = 0,
        negative_slope: float = 0.2,
        edge_dim: int | None = None,
    ):
        '''
        GAT initialization.

        :param input_dim: dimensionality of an input vector
        :param hidden_dim: dimensionality of vectors in hidden layers
        :param num_heads: number of attention heads
        :param num_layers: number of hidden convolutional layers (per each attention head)
        :param dropout: dropout rate
        :param negative_slope: slope coefficient for LeakyReLU layers of attention heads
        :param edge_dim: dimensionality of edge attribute vectors
        '''

        super().__init__()

        self.dropout = dropout

        self.convs = nn.ModuleList()
        for i in range(num_layers):
            in_dim = hidden_dim if i else input_dim
            self.convs.append(pyg_nn.Sequential('x, edge_index, edge_attr', [
                (pyg_nn.convs.GATv2Conv(
                    in_dim,
                    hidden_dim,
                    num_heads,
                    concat=False,
                    edge_dim=edge_dim,
                    negative_slope=negative_slope,
                ), 'x, edge_index, edge_attr -> x'),
                pyg_nn.norm.GraphNorm(in_channels=hidden_dim),
                nn.PReLU(num_parameters=hidden_dim),
            ]))

        self.post_mp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Dropout(dropout),
            nn.PReLU(num_parameters=hidden_dim),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid(),
        )

    def forward(self, data: DataBatch) -> Tensor:
        '''
        Apply a forward pass for a data batch.

        :param data: torch_geometric.data.batch.DataBatch instance to process
        :return: torch.Tensor with class probabilities for each data instance in a batch
        '''

        x, edge_index, edge_attr, batch = data.x, data.edge_index, data.edge_attr, data.batch

        for conv in self.convs:
            x = conv(x, edge_index, edge_attr)
        x = pyg_nn.global_max_pool(x, batch)
        x = self.post_mp(x)

        return x


def train_gnn(
    model: nn.Module,
    train_loader: DataLoader,
    n_epochs: int,
    optimizer: Optimizer,
    scheduler: LRScheduler | None = None,
    eval_loss: Callable[[Tensor, Tensor], Tensor] = fn.binary_cross_entropy,
    val_loader: DataLoader | None = None,
    *,
    verbose: bool = True,
) -> tuple[nn.Module, list[float], list[float], list[float]]:
    '''
    Train a graph neural network classifier.

    :param model: model to train
    :param train_loader: data loader for training
    :param n_epochs: number of epochs to train a model for
    :param optimizer: PyTorch Optimizer instance
    :param scheduler: PyTorch LRScheduler instance
    :param eval_loss: callback to evaluate loss function on a data batch
    :param val_loader: data loader for validation
    :param verbose: verbosity flag
    :return: trained model, list of mean batch loss per training epoch, \
        list of train accuracy values, and list of validation accuracy values
    '''

    train_loss = []
    train_accuracy = []
    val_accuracy = []

    device = next(model.parameters()).device
    train_size = len(train_loader.dataset)
    val_size = len(val_loader.dataset) if val_loader is not None else 0

    with tqdm(range(n_epochs), desc='Training GNN...', total=n_epochs, disable=not verbose) as bar:
        for epoch in bar:
            batch_train_loss = []
            batch_train_accuracy = 0
            batch_val_accuracy = 0

            model.train()
            for batch in train_loader:
                batch = batch.to(device)
                logits = model(batch)[:, 0]
                labels = batch.y.type(torch.float)

                loss = eval_loss(logits, labels)

                loss.backward()
                optimizer.step()
                if scheduler is not None:
                    scheduler.step()
                optimizer.zero_grad()

                batch_train_loss.append(float(loss.data.numpy()))
                pred = (logits > 0.5)
                batch_train_accuracy += (labels == pred).numpy().sum()
            train_loss.append(float(np.mean(batch_train_loss)))
            train_accuracy.append(batch_train_accuracy / train_size)

            if val_loader is not None:
                model.eval()
                for batch in val_loader:
                    batch = batch.to(device)
                    logits = model(batch)[:, 0]
                    labels = batch.y.type(torch.float)
                    pred = (logits > 0.5)
                    batch_val_accuracy += (labels == pred).numpy().sum()
                val_accuracy.append(batch_val_accuracy / val_size)

                bar.set_postfix(
                    loss=f'{train_loss[-1]:.4f}',
                    train_acc=f'{train_accuracy[-1] * 100:.4f}',
                    val_acc=f'{val_accuracy[-1] * 100:.4f}',
                )
            else:
                bar.set_postfix(
                    loss=f'{train_loss[-1]:.4f}',
                    train_acc=f'{train_accuracy[-1] * 100:.4f}',
                )

    return model, train_loss, train_accuracy, val_accuracy
