import pathlib
from pkg_resources import resource_filename


def get_root_path():
    import gaffils
    return pathlib.Path(gaffils.__file__).parent


def load_GAFFILS():
    from foyer import Forcefield
    path = pathlib.Path(str(get_root_path()) + '/xml/gaffils.xml')
    return Forcefield(path)

