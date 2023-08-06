import importlib
import builtins

__all__ = ['VariableSpecifier']


class VariableSpecifier(object):

    class __NotResolved:
        pass

    @property
    def variable(self):

        if self._variable is self.__NotResolved:
            if self._variable_module:
                module = importlib.import_module(self._variable_module)
            else:
                module = builtins

            self._variable = getattr(module, self._variable_name, lambda: list())

        return self._variable

    @property
    def variable_path(self):
        return self._variable_path

    def __init__(self, *, variable_path):
        super().__init__()
        self._variable_path = variable_path

        parts = self._variable_path.rsplit('.', maxsplit=1)

        if len(parts) == 2:
            self._variable_module = parts[0]
            self._variable_name = parts[1]
        else:
            self._variable_module = None
            self._variable_name = parts[0]

        self._variable = self.__NotResolved
