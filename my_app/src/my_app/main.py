import logging
import os

import requests

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


def download_file(url: str, filename: str = 'latest.csv') -> None:
    try:
        response = fetch_data(url)

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        file_path = os.path.join(project_root, filename)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        logging.info(f'Plik został zapisany jako: {filename}')

    except (NotFoundError, AccessDeniedError, HTTPError) as e:
        logging.error(f'Błąd HTTP: {e}')


if __name__ == '__main__':
    download_file(
        'https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv'
    )
