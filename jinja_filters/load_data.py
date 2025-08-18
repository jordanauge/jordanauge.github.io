import pathlib
import yaml

def load_data(name):
    p = pathlib.Path(__file__).parent.parent
    data_file = p / 'data' / f'{name}.yaml'
    with data_file.open() as f:
        return yaml.safe_load(f)
