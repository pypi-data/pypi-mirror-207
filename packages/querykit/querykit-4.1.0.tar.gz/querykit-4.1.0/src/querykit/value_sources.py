from django.utils.deconstruct import deconstructible

__all__ = ['ValueSource', 'PathValueSource', 'UnsupportedValueSource']


class UnsupportedValueSource(RuntimeError):
    pass


@deconstructible
class ValueSource:

    @property
    def value_type(self):
        return self._value_type

    def __init__(self, *, value_type):
        self._value_type = value_type


class PathValueSource(ValueSource):

    @property
    def path(self):
        return self._path

    @property
    def label_path(self):
        return self._label_path if self._label_path else self._path

    def __init__(self, *, value_type, path, label_path=None, **kwargs):
        super().__init__(value_type=value_type)

        self._path = path
        self._label_path = label_path