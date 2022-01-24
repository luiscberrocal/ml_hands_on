import tarfile
import urllib.request
from pathlib import Path

DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml2/master'
# DOWNLOAD_ROOT = 'https://github.com/ageron/handson_ml2/master'
HOUSING_PATH = Path(__file__).parent / 'data' / 'housing'
HOUSING_URL = f'{DOWNLOAD_ROOT}/datasets/housing/housing.tgz'


def download_housing_data(housing_url: str = HOUSING_URL, housing_path: 'Path' = HOUSING_PATH):
    print(f'url: {housing_url}')
    housing_path.mkdir(exist_ok=True, parents=True)
    tar_path = housing_path / 'housing.tgz'
    urllib.request.urlretrieve(housing_url, tar_path)
    housing_tar = tarfile.open(tar_path)
    housing_tar.extractall(path=housing_path)
    housing_tar.close()


if __name__ == '__main__':
    download_housing_data()
