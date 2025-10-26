import os

from my_app.utils import download_file, get_file_path, count_sum_avg, count_dash_indices


def download_transform_file(url: str, file_name: str = 'latest.csv') -> None:
    file_path = get_file_path(file_name)
    download_file(url, file_path)

    with open(file_path, 'r') as file:
        content = file.read()

    lines = content.strip().splitlines()

    with (open(get_file_path('values.csv'), 'w') as f1, open(get_file_path('missing_values.csv'), 'w') as f2):
        for line in lines:
            row = line.split(',')

            total, avg = next(count_sum_avg(row))
            f1.write(f'{row[0]}, {total}, {avg}\n')

            missing = next(count_dash_indices(row))
            f2.write(f'{row[0]}, {', '.join(map(str, missing))}\n')


if __name__ == '__main__':
    download_transform_file(
        'https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv'
    )
