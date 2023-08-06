'''Fetching standard (built-in) models.'''

from itertools import repeat
from multiprocessing import cpu_count, Pool
import os
from pathlib import Path
from urllib.parse import urlencode

import requests
from tqdm import tqdm

from .exception import FetchError
from .logger import get_logger


__all__ = (
    'download',
    'download_all',
    'get_model_path',
)


logger = get_logger(__name__)


CURDIR = Path(os.path.relpath(__file__)).parent
MODELS_DIR = CURDIR / 'models'

BASE_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
FILE_NAMES = {
    'udpipe': 'russian-syntagrus-ud-2.5-191206.udpipe',
    'cbow': 'ruwikiruscorpora_upos_cbow_300_2021.txt',
    'elmo1024': 'ruwikiruscorpora_lemmas_elmo_1024_2019.zip',
    'elmo2048': 'araneum_lemmas_elmo_2048_2020.zip',
    'gcn': 'gcn_model.pth',
    'gat': 'gat_model.pth',
}
FILE_URLS = {
    'udpipe': 'https://disk.yandex.ru/d/Pz17-vtNeasApg',
    'cbow': 'https://disk.yandex.ru/d/6dXzkn0r9Otjnw',
    'elmo1024': 'https://disk.yandex.ru/d/mIZRldOR6B16rw',
    'elmo2048': 'https://disk.yandex.ru/d/fAl1ON3JKmWwDQ',
    'gcn': 'https://disk.yandex.ru/d/kI010Uqj2F51zw',
    'gat': 'https://disk.yandex.ru/d/9_0I88hnEz2G0w',
}
CHUNK_SIZE = 8_192


def get_model_path(file: str) -> Path:
    '''
    Get path to a built-in model if present.

    :param file: model name to find a file for
    :return: path to a model
    '''

    filename = FILE_NAMES.get(file)
    if filename is None:
        raise FetchError(f'Unknown filename "{file}".')
    return MODELS_DIR / filename


def fetch_url(file: str) -> requests.Response:
    '''
    URL fetching worker.

    :param file: filename to fetch
    :return: requests.Response instance
    '''

    file_url = FILE_URLS.get(file)
    if file_url is None:
        raise FetchError(f'Cannot fetch url for file "{file}".')

    api_url = BASE_URL + urlencode(dict(public_key=file_url))
    response = requests.get(api_url)
    download_url = response.json()['href']

    download_response = requests.get(download_url, stream=True)
    if not download_response:
        raise FetchError(
            f'Failed to fetch url for file "{file}": '
            f'HTTP status code {download_response.status_code}'
        )
    return download_response


def download_all(*, verbose: bool = True, force: bool = False) -> None:
    '''
    Download all built-in models in parallel.

    :param verbose: verbosity flag
    :param force: whether to force downloading existing files
    :return: None
    '''

    num_workers = min(cpu_count(), len(FILE_NAMES))
    with Pool(num_workers) as pool:
        pool.starmap(download, zip(FILE_NAMES, repeat(verbose), repeat(force)))


def download(file: str, *, verbose: bool = True, force: bool = False) -> None:
    '''
    Download a built-in model.

    :param file: model name to download
    :param verbose: verbosity flag
    :param force: whether to force downloading existing files
    :return: None
    '''

    if file == 'elmo':
        download('elmo1024')
        download('elmo2048')
        return
    if file == 'neural':
        download('gcn')
        download('gat')
        return

    MODELS_DIR.mkdir(exist_ok=True)
    path = get_model_path(file)
    if not path.exists() or force:
        if verbose:
            logger.info(f'Downloading "{file}"...')

        response = fetch_url(file)
        total = response.headers.get('content-length')
        content = response.iter_content(chunk_size=CHUNK_SIZE)
        bar = tqdm(
            desc=f'Downloading "{file}"...',
            total=int(total) if total is not None else None,
            disable=not verbose,
        )

        with open(path, 'wb') as fout:
            for chunk in content:
                fout.write(chunk)
                bar.update(len(chunk))
        bar.close()
    elif verbose:
        logger.info(f'File "{file}" already exists. Set force=True to proceed anyway.')
    else:
        pass
