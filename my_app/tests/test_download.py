import os

from my_app.main import download_file


def test_download_file_creates_file():
    test_url = 'https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv'
    test_filename = 'latest.csv'

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(project_root, test_filename)

    if os.path.exists(test_filename):
        os.remove(file_path)

    download_file(test_url, file_path)

    assert os.path.exists(test_filename)

    os.remove(test_filename)
