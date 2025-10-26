import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)


def download_file(url: str, filename: str = 'latest.csv') -> None:
    response = requests.get(url)

    with open(f'../../{filename}', 'wb') as file:
        file.write(response.content)

    logging.info(f'Plik został zapisany jako: {filename}')


if __name__ == '__main__':
    download_file(
        'https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv'
    )
