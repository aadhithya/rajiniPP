import yaml
from munch import DefaultMunch


def read_yml(yml_path: str) -> DefaultMunch:
    """
    read_yml read yaml file and return munch object.

    Args:
        yml_path (str): path to yml file.

    Returns:
        DefaultMunch: yaml contents.
    """
    with open(yml_path, "r") as f:
        yml = yaml.safe_load(f)

    return DefaultMunch.fromDict(yml)
