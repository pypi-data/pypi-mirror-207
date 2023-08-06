'''CLI tool implementation.'''

from pathlib import Path
from typing import Any

import click

from .. import (
    IdentitySentenceFilter, MinLengthSentenceFilter,
    PairwiseOrderHeuristic, JaccardIndexOrderHeuristic,
    SABK, TABK, MSK, CompositeKernel, AssignmentKernel, NeuralKernel,
    UDPipeSyntaxParser, AutoEmbeddingModel, CBOWModel,
    TextEngine, SemSimEngine,
    ArgumentError,
)
from ..algo.kernel import DISTANCES
from ..download import download_all, download as download_one


__all__ = (
    'compare',
    'download',
)


FILTER_TYPE_TO_CLS = {
    'id': IdentitySentenceFilter,
    'min-length': MinLengthSentenceFilter,
}

HEURISTIC_TYPE_TO_CLS = {
    'pairwise': PairwiseOrderHeuristic,
    'jaccard': JaccardIndexOrderHeuristic,
}

KERNEL_TYPE_TO_CLS = {
    'sabk': SABK,
    'tabk': TABK,
    'msk': MSK,
    'ck': CompositeKernel,
    'ak': AssignmentKernel,
    'nk': NeuralKernel,
    'composite': CompositeKernel,
    'assignment': AssignmentKernel,
    'neural': NeuralKernel,
}


def filter_none_values(dct: dict[str, Any]) -> dict[str, Any]:
    '''
    Filter out dictionary entries with None values.

    :param dct: dictionary to filter
    :return: filtered dictionary instance
    '''

    return {
        key: value
        for key, value in dct.items()
        if value is not None
    }


@click.group()
def cli() -> None:
    '''CLI group.'''

    pass


@cli.command()
@click.argument(  # texts to compare
    'first_src',
    type=click.Path(dir_okay=False, readable=True),
)
@click.argument(
    'second_src',
    type=click.Path(dir_okay=False, readable=True),
)
@click.option(  # syntax parser model
    '-s', '--syntax', 'syntax_path',
    type=click.Path(dir_okay=False, readable=True),
    help='Path to the UDPipe syntax model.',
)
@click.option(  # embedding model
    '-e', '--embs_type',
    type=click.Choice(['cbow', 'elmo1024', 'elmo2048', 'none'], case_sensitive=False),
    help='Embedding model type.',
)
@click.option(
    '--cbow_path',
    type=click.Path(dir_okay=False, readable=True),
    help='Path to a CBOW embedding model.',
)
@click.option(
    '-v/-q', '--verbose/--quiet',
    is_flag=True,
    default=True,
    show_default=True,
    help='Verbosity flag.',
)
@click.option(  # filter
    '-f', '--filter', 'filter_type',
    type=click.Choice(['id', 'min-length'], case_sensitive=False),
    default='min-length',
    show_default=True,
    help='Sentence filter type.',
)
@click.option(
    '--min-length',
    type=click.IntRange(min=1),
    help='Min length of sentences in tokens (for "min-length" filter only).',
)
@click.option(  # pair order heuristic
    '--heuristic', 'heuristic_type',
    type=click.Choice(['jaccard', 'pairwise'], case_sensitive=False),
    default='pairwise',
    show_default=True,
    help='Pair selection heuristic type.',
)
@click.option(
    '--min-jaccard',
    type=click.FloatRange(0, 1),
    help='Min Jaccard index value for filtering sentence pairs.',
)
@click.option(
    '--jaccard-lemma/--no-jaccard-lemma',
    is_flag=True,
    help='Use lemmas for jaccard index order heuristic.',
)
@click.option(  # kernel parameters
    '-k', '--kernel', 'kernel_type',
    type=click.Choice([
            'sabk', 'tabk', 'msk', 'ck', 'ak', 'nk',
            'composite', 'assignment', 'neural',
        ],
        case_sensitive=False,
    ),
    default='composite',
    show_default=True,
    help='Kernel type.',
)
@click.option(
    '--cmp-lemma/--no-cmp-lemma',
    is_flag=True,
    help='Compare lemmas instead of tokens in bigram kernels.',
)
@click.option(
    '--emb-metric',
    type=click.Choice(list(DISTANCES.keys()), case_sensitive=False),
    help='Embedding distance metric.',
)
@click.option(
    '-p',
    type=click.FloatRange(min=0, min_open=True),
    help='Parameter "p" for Minkowski distance.',
)
@click.option(
    '--theta',
    type=click.FloatRange(min=1),
    help='Parameter "theta" for dependency relation distance.',
)
@click.option(
    '--lambda', 'lambda_',
    type=click.FloatRange(min=0),
    help='Parameter "lambda" for dependency relation distance.',
)
@click.option(
    '--gamma',
    type=click.FloatRange(min=0, max=1, min_open=True),
    help='Parameter "gamma" for additive kernels.',
)
@click.option(
    '--idf-path',
    type=click.Path(dir_okay=False, readable=True),
    help='Path to an idf dictionary for TABK kernel.',
)
@click.option(
    '--unknown-idf',
    type=click.FloatRange(min=0),
    help='IDF value of unknown tokens for TABK kernel.',
)
@click.option(
    '--use-lemma/--no-use-lemma',
    is_flag=True,
    help='Use lemmas in TABK kernel.',
)
@click.option(
    '--alpha',
    type=click.FloatRange(min=0, max=1, min_open=True),
    help='Parameter "alpha" for MSK kernel.',
)
@click.option(
    '--nu',
    type=click.FloatRange(min=0, max=1, max_open=True),
    help='Parameter "nu" for MSK kernel.',
)
@click.option(
    '--beta',
    type=click.FloatRange(min=0, max=1),
    help='Parameter "beta" for CK kernel.',
)
@click.option(
    '--delta',
    type=click.FloatRange(min=0, max=1),
    help='Parameter "delta" for CK kernel.',
)
@click.option(
    '--gnn-path',
    type=click.Path(dir_okay=False, readable=True),
    help='Path to a PyTorch GNN model save (checkpoint).',
)
@click.option(
    '--gnn-type',
    type=click.Choice(['gcn', 'gat'], case_sensitive=False),
    help='GNN architecture type.',
)
@click.option(
    '--batch-size',
    type=click.IntRange(min=1),
    help='Batch size for GNN (in batched processing mode).',
)
@click.option(
    '--device',
    type=str,
    help='Type of device to load a GNN model and batches to.',
)
@click.option(  # additional SemSimEngine parameters
    '--max-out-pairs',
    type=click.IntRange(min=1),
    help='Max number of similar tree pairs to output.',
)
@click.option(
    '--max-process-pairs',
    type=click.IntRange(min=1),
    help='Max number of tree pairs to process.',
)
@click.option(
    '-o', '--output',
    type=click.Path(dir_okay=False, writable=True, readable=False),
    help='Output file path (stdout by default).',
)
def compare(
    first_src: str | Path,
    second_src: str | Path,

    syntax_path: str | Path | None,

    embs_type: str | None,
    cbow_path: str | Path | None,

    verbose: bool,

    filter_type: str,
    min_length: int | None,

    heuristic_type: str,
    min_jaccard: float | None,
    jaccard_lemma: bool | None,

    kernel_type: str,
    cmp_lemma: bool | None,
    emb_metric: str | None,
    p: float | None,
    theta: float | None,
    lambda_: float | None,
    gamma: float | None,
    idf_path: str | Path | None,
    unknown_idf: float | None,
    use_lemma: bool | None,
    alpha: float | None,
    nu: float | None,
    beta: float | None,
    delta: float | None,
    gnn_path: str | Path | None,
    gnn_type: str | None,
    batch_size: int | None,
    device: str | None,

    max_out_pairs: int | None,
    max_process_pairs: int | None,
    output: str | Path | None,
) -> None:
    '''CLI `compare` subcommand implementation.'''

    syntax_parser = UDPipeSyntaxParser(
        model_path=syntax_path,
    )

    if cbow_path is not None:
        if embs_type is not None:
            raise ArgumentError(
                'You should specify either "embs_type" or "cbow_path" '
                'parameter, but not both.'
            )
        cbow_model = CBOWModel(cbow_path)
        emb_model = AutoEmbeddingModel(static_model=cbow_model)
    else:
        if embs_type == 'none':
            embs_type = None
        emb_model = AutoEmbeddingModel(embs_type=embs_type)

    filter_cls = FILTER_TYPE_TO_CLS.get(filter_type)
    if filter_cls is None:
        raise ArgumentError(f'Unknown filter type "{filter_type}"')
    filter_params = filter_none_values({
        'min_length': min_length,
    })
    sentence_filter = filter_cls(**filter_params)

    engine = TextEngine(
        syntax_parser=syntax_parser,
        emb_model=emb_model,
        sentence_filter=sentence_filter,
    )

    heuristic_cls = HEURISTIC_TYPE_TO_CLS.get(heuristic_type)
    if heuristic_cls is None:
        raise ArgumentError(f'Unknown heuristic type "{heuristic_type}"')
    heuristic_params = filter_none_values({
        'min_jaccard': min_jaccard,
        'use_lemma': jaccard_lemma,
    })
    heuristic = heuristic_cls(**heuristic_params)

    idf = None
    if idf_path is not None:
        with open(idf_path, 'r', encoding='utf-8') as file:
            idf = {}
            for line in file:
                key, value = line.split(':')
                idf[key] = float(value)

    kernel_cls = KERNEL_TYPE_TO_CLS.get(kernel_type)
    if kernel_cls is None:
        raise ArgumentError(f'Unknown kernel type "{kernel_type}"')
    kernel_params = filter_none_values({
        'cmp_lemma': cmp_lemma,
        'emb_metric': emb_metric,
        'p': p,
        'theta': theta,
        'lambda_': lambda_,
        'gamma': gamma,
        'idf': idf,
        'unknown_idf': unknown_idf,
        'use_lemma': use_lemma,
        'alpha': alpha,
        'nu': nu,
        'beta': beta,
        'delta': delta,
        'gnn_path': gnn_path,
        'gnn_type': gnn_type,
        'batch_size': batch_size,
        'device': device,
    })
    kernel = kernel_cls(**kernel_params)

    semsim_engine_params = filter_none_values({
        'engine': engine,
        'kernel': kernel,
        'heuristic': heuristic,
        'verbose': verbose,
        'max_out_pairs': max_out_pairs,
        'max_process_pairs': max_process_pairs,
    })
    semsim_engine = SemSimEngine(**semsim_engine_params)

    results = semsim_engine.find_top_closest_sentences(Path(first_src), Path(second_src))

    if output is None:
        for idx, cmp in enumerate(results, start=1):
            print(f'Sentence pair #{idx}\n{cmp}', end='\n\n')
    else:
        with open(output, 'w', encoding='utf-8') as file:
            for idx, cmp in enumerate(results, start=1):
                print(f'Sentence pair #{idx}\n{cmp}', end='\n\n', file=file)


@cli.command()
@click.option(
    '-m', '--file', '--model',
    type=str,
    help='Model name',
)
@click.option(
    '-v/-q', '--verbose/--quiet',
    is_flag=True,
    default=True,
    show_default=True,
    help='Verbosity flag.',
)
@click.option(
    '-f', '--force',
    is_flag=True,
    default=False,
    show_default=True,
    help='Whether to force downloading already existing files.',
)
@click.option(
    '-a', '--all',
    is_flag=True,
    default=False,
    show_default=True,
    help='Pass this to download all built-in models at once.',
)
def download(
    file: str | None,
    verbose: bool,
    force: bool,
    all: bool,
) -> None:
    '''CLI `download` subcommand implementation.'''

    if all:
        if file is not None:
            raise ArgumentError('Cannot pass "file" argument along with "--all" flag.')
        download_all(verbose=verbose, force=force)
    elif file is None:
        raise ArgumentError('You should pass either "file" argument or "--all" flag, but not both.')
    else:
        download_one(file, verbose=verbose, force=force)


if __name__ == '__main__':
    cli()
