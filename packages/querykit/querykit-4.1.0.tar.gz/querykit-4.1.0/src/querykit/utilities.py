import importlib

__all__ = ['construct']


def construct(path, args, kwargs):
    module_name, clname = path.rsplit(sep=".", maxsplit=1)
    clmodule = importlib.import_module(module_name)
    path_class = getattr(clmodule, clname)
    return path_class(*args, **kwargs)
