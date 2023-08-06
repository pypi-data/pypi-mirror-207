# -*- coding: utf-8 -*-

import re
import unicodedata

from urllib.parse import quote_plus

from django.utils.deconstruct import deconstructible
from django.utils.encoding import force_str

from datetime import date, datetime

__all__ = ['ValueType', 'CharType', 'TextType', 'BooleanType', 'IntegerType', 'FloatType',
           'DateType', 'DateTimeType', 'ValueIdentifierMap']


class UnknownValueTypeError(RuntimeError):
    pass


VALUE_TYPE_REGISTRY = {}


@deconstructible
class ValueType:

    @property
    def identifier(self):
        return self._identifier

    @property
    def default_value(self):
        return self._default_value

    def __init__(self, identifier, *, default_value, base_types=None, unpack=None, pack=None):

        if base_types is None:
            base_types = []

        self._identifier = identifier
        self._default_value = default_value
        self._base_types = list(base_types)
        self._unpack = unpack
        self._pack = pack

    def derived_from(self, value_type):
        return False

    def pack(self, value):
        return value if self._pack is None else self._pack(value)

    def unpack(self, value):
        return value if self._unpack is None else self._unpack(value)

    @staticmethod
    def define(identifier, *, default_value=None, base_types=None, pack=None, unpack=None):

        value_type = ValueType(identifier, default_value=default_value, base_types=base_types, pack=pack, unpack=unpack)
        VALUE_TYPE_REGISTRY[identifier] = value_type
        return value_type

    @staticmethod
    def lookup(identifier, default=None):
        return VALUE_TYPE_REGISTRY.get(identifier, default)


def simplify_character(char):

    """
    Return the base character of char, by "removing" any
    diacritics like accents or curls and strokes and the like.
    """

    name = unicodedata.name(char)
    limit = name.find(' WITH ')

    if limit <= 0:
        return char

    name = name[:limit]

    try:
        char = unicodedata.lookup(name)
    except KeyError:
        pass

    return char


class AddMissingIdentifier:
    pass


class ValueIdentifierMap:

    class __Missing:
        pass

    def __init__(self):
        self.__identifier_to_value = {}
        self.__value_to_identifier = {}

    def __len__(self):
        return len(self.__identifier_to_value)

    def __contains__(self, identifier):
        return identifier in self.__identifier_to_value

    def identifiers(self):
        return self.__identifier_to_value.keys()

    def values(self):
        return self.__value_to_identifier.keys()

    def identifier_to_value(self, identifier, default=None):
        return self.__identifier_to_value.get(identifier, default)

    WHITESPACE_RE = re.compile(r'\s+')
    HYPHEN_RE = re.compile(r'-+')

    def derive_identifier_from_value(self, value):

        value = force_str(value)
        identifier = "".join([simplify_character(c) for c in value.lower()])

        identifier = self.WHITESPACE_RE.sub('-', identifier)
        identifier = self.HYPHEN_RE.sub('-', identifier)
        identifier = quote_plus(identifier)
        return identifier

    def value_to_identifier(self, value, default=AddMissingIdentifier):

        identifier = self.__value_to_identifier.get(value, self.__Missing)

        if identifier is not self.__Missing:
            return identifier

        if default is not AddMissingIdentifier:
            return default

        # This value has no identifier

        base_identifier = self.derive_identifier_from_value(value)
        identifier = base_identifier
        n = 1

        while True:

            mapped_value = self.__identifier_to_value.get(identifier, self.__Missing)

            if mapped_value is self.__Missing:
                break

            if mapped_value == value:
                return identifier

            n += 1

            identifier = "{}-{:d}".format(base_identifier, n)

        self.__identifier_to_value[identifier] = value
        self.__value_to_identifier[value] = identifier

        return identifier


CharType = ValueType.define("char", default_value="")
TextType = ValueType.define("text", default_value="")
BooleanType = ValueType.define("boolean", default_value=False)
IntegerType = ValueType.define("integer", default_value=0, pack=str, unpack=int)
FloatType = ValueType.define("float", default_value=0, pack=str, unpack=float)
DateType = ValueType.define("date", default_value=0, pack=str, unpack=date)
DateTimeType = ValueType.define("datetime", default_value=0, pack=str, unpack=datetime)


