import logging
import os

import requests

from typing import Generator

from my_app.exceptions import HTTPError, NotFoundError, AccessDeniedError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)


def fetch_data(url: str) -> requests.Response:
    response = requests.get(url)

    if response.status_code == 404:
        raise NotFoundError()
    elif response.status_code == 403:
        raise AccessDeniedError()
    elif response.status_code >= 400:
        raise HTTPError(response.status_code)

    return response


def download_file(url: str, file_path: str, file_name: str = 'latest.csv') -> None:
    try:
        response = fetch_data(url)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        logging.info(f'Plik został zapisany jako: {file_name}')

    except (NotFoundError, AccessDeniedError, HTTPError) as e:
        logging.error(f'Błąd HTTP: {e}')


def get_file_path(file_name: str) -> str:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.join(project_root, file_name)


def count_sum_avg(line: list) -> Generator[tuple[float, float], None, None]:
    values = [float(val) for i, val in enumerate(line) if i > 0 and val != '-']
    total = sum(values)
    avg = total / len(values)

    yield round(total, 2), round(avg, 2)


def count_dash_indices(line: list) -> Generator[list[int], None, None]:
    yield [i - 1 for i, val in enumerate(line) if i > 0 and val == '-']
