
from django.apps import apps
from django.core import exceptions
from django.db.models import Model, Q, When, Count, Value, F, Value as V
from django.db.models.functions import Cast, Concat
from django.db.models import TextField, CharField
from django.utils.encoding import force_str
from django.utils.functional import cached_property

from .base import QueryEngine, QueryExecution, QueryResult, QueryResultSlice, \
    SliceNumberNotNumeric, SliceNumberOutOfRange, Filter, ResultSliceParameter, OrderParameter, SliceSizeParameter

from .value_types import *
from .value_sources import *

from .apps import get_app_label

__all__ = ['DjangoQueryEngine', 'DjangoQueryExecution']

APP_LABEL = get_app_label()


class DjangoSlice(QueryResultSlice):

    @property
    def result(self):
        return self._result

    @property
    def object_list(self):
        return self._queryset

    @property
    def number(self):
        return self._number

    @property
    def is_first(self):
        return self._number == 1

    @property
    def is_last(self):
        return self.number >= self.result.total_slice_count

    @property
    def is_only_slice(self):
        return self.is_first and self.is_last

    @property
    def is_empty(self):
        return not self._queryset

    @property
    def slice_object_count(self):
        return len(self._queryset)

    @property
    def first_object_index(self):
        return (self.number - 1) * self.result.slice_size + 1

    @property
    def last_object_index(self):
        return self.first_object_index + len(self._queryset) - 1

    def __init__(self, *, result, queryset, number):
        super().__init__()

        self._result = result
        self._queryset = queryset
        self._number = number


class DjangoQueryResult(QueryResult):

    @property
    def query(self):
        return self._query

    @property
    def object_list(self):
        return self._queryset

    @property
    def total_object_count(self):
        return self._queryset.count()

    @property
    def total_slice_count(self):

        if not self.slice_size:
            return 1

        return (self.total_object_count + self.slice_size - 1) // self.slice_size

    @property
    def slice_number_range(self):
        return range(1, self.total_slice_count + 1)

    @property
    def slice_size(self):
        return self._slice_size

    def __init__(self, *, query, queryset, empty_queryset, slice_size=10, **kwargs):
        super(DjangoQueryResult, self).__init__(**kwargs)
        self._query = query
        self._queryset = queryset
        self._empty_queryset = empty_queryset
        self._slice_size = slice_size

    def slice_for_number(self, number):

        number = self.__clean_number(number)
        slice_queryset = self.__queryset_for_slice_number(number)
        query_slice = self.__create_slice(result=self, queryset=slice_queryset, number=number)
        return query_slice

    def empty_slice(self):

        query_slice = self.__create_slice(result=self, queryset=self._empty_queryset, number=1)
        return query_slice

    # noinspection PyMethodMayBeStatic
    def __create_slice(self, **kwargs):
        return DjangoSlice(**kwargs)

    def __queryset_for_slice_number(self, number):

        if number < 1:
            raise SliceNumberOutOfRange

        if number > self.total_slice_count:
            raise SliceNumberOutOfRange

        if not self.slice_size or self.total_slice_count == 1:
            return self._queryset

        return self._queryset[(number - 1) * self.slice_size:number * self.slice_size]

    def __clean_number(self, number):

        try:
            number = int(number)
        except (ValueError, TypeError):
            raise SliceNumberNotNumeric

        if number < 1:
            raise SliceNumberOutOfRange

        if number > self.total_slice_count:
            raise SliceNumberOutOfRange

        return number


class DjangoQueryExecution(QueryExecution):

    @property
    def filters(self):
        return self._filters

    @property
    def order_by(self):
        return self._order_by

    @property
    def slice_number(self):
        return self._slice_number

    @slice_number.setter
    def slice_number(self, value):
        self._slice_number = value

    @property
    def slice_size(self):
        return self._slice_size

    @slice_size.setter
    def slice_size(self, value):
        self._slice_size = value

    def __init__(self, *, model_class, queryset=None, slice_size=None, slice_number=1, query, **kwargs):

        super(DjangoQueryExecution, self).__init__(**kwargs)

        self._model_class = model_class
        self._queryset = queryset
        self._slice_size = slice_size
        self._slice_number = slice_number
        self._filters = []
        self._order_by = []
        self._query = query

    def run(self) -> QueryResultSlice:

        empty_queryset = self._model_class.objects.none()

        queryset = self._model_class.objects.all() if self._queryset is None else self._queryset.all()

        if self.filters:
            queryset = queryset.filter(*self.filters)

        if self.order_by:
            queryset = queryset.order_by(*self.order_by)

        slice_size = self._slice_size

        if not slice_size:
            slice_size = queryset.count()

        result = DjangoQueryResult(query=self._query,
                                   queryset=queryset, empty_queryset=empty_queryset, slice_size=slice_size)

        if 1 <= self.slice_number <= result.total_slice_count:
            result_slice = result.slice_for_number(self.slice_number)
        else:
            result_slice = result.empty_slice()

        return result_slice


class DjangoQueryEngine(QueryEngine):

    @cached_property
    def model_class(self):
        return resolve_model_string(self.target_model)

    def __init__(self, *, target_model, **kwargs):
        self.target_model = target_model
        self.value_maps = {}

        super(DjangoQueryEngine, self).__init__(**kwargs)

    def construct_execution_for(self, *, query, **kwargs):

        result = DjangoQueryExecution(model_class=self.model_class, query=query, **kwargs)

        parameter_map = query.handler.parameter_map

        for setting in query.settings:

            entry = parameter_map.get(setting.identifier, None)

            if entry is None:
                continue

            self.apply_parameter(entry.parameter, setting, result)

        return result

    def apply_parameter(self, parameter, setting, execution):
        # Here is where all the magic happens

        if isinstance(parameter, Filter):
            self.apply_filter(parameter, setting, execution)

        if isinstance(parameter, ResultSliceParameter):
            self.apply_result_slice_parameter(parameter, setting, execution)

        if isinstance(parameter, SliceSizeParameter):
            self.apply_slice_size_parameter(parameter, setting, execution)

        if isinstance(parameter, OrderParameter):
            self.apply_order(parameter, setting, execution)

    # noinspection PyMethodMayBeStatic
    def apply_result_slice_parameter(self, parameter, setting, execution):

        if not setting.value_list:
            return

        if setting.value_list[0] < 1:
            return

        execution.slice_number = setting.value_list[0]

    # noinspection PyMethodMayBeStatic
    def apply_slice_size_parameter(self, parameter, setting, execution):

        if not setting.value_list or not setting.value_list[0]:
            value = parameter.size_choices[0][0]
        else:
            value = setting.value_list[0]

        if value == 'all':
            value = None
        elif value < 1:
            value = 1
        elif value > 100:
            value = 100

        execution.slice_size = value

    # noinspection PyMethodMayBeStatic
    def apply_filter(self, filter, setting, execution):

        if not setting.value_list:
            return

        argument = self.create_filter_argument(
            setting.value_list, filter.value_source)

        execution.filters.append(argument)

    # noinspection PyMethodMayBeStatic
    def apply_order(self, parameter, setting, execution):

        if not setting.value_list:
            return

        order_specifier = parameter.order_specifier_map.get(setting.value_list[0], None)

        if order_specifier is None:
            return

        for value_source in order_specifier.value_sources:

            value_lookup = self.field_value_lookup_from_value_source(value_source)
            execution.order_by.append(value_lookup)

    # noinspection PyMethodMayBeStatic
    def create_filter_argument(self, value_identifier_list, value_source):

        value_type = value_source.value_type
        value_lookup = self.field_value_lookup_from_value_source(value_source)
        value_map = self.value_maps.get(value_lookup, None)

        if value_map is None:
            _ = list(self.select_frequent_values_from(value_source, include_labels=True, limit=100))
            value_map = self.value_maps.get(value_lookup, None)

            if value_map is None:
                value_map = ValueIdentifierMap()
                self.value_maps[value_lookup] = value_map

        value_list = [value_type.unpack(value_map.identifier_to_value(identifier)) for identifier in value_identifier_list if identifier in value_map]
        value_list = [value for value in value_list if value is not None]

        union = []

        if value_source.value_type is TextType:
            value_lookup += "__icontains"

        for value in value_list:

            if value_source.value_type is TextType:
                and_values = value.split()

                if len(and_values) > 1:

                    intersection = []

                    for and_value in and_values:
                        intersection.append(Q(**dict(((value_lookup, and_value),))))

                    intersection_result = intersection[0]

                    for index in range(1, len(intersection)):
                        intersection_result = intersection_result & intersection[index]

                    union.append(intersection_result)
                    continue

            union.append(Q(**dict(((value_lookup, value),))))

        if len(union) == 0:
            value_lookup = self.field_value_lookup_from_value_source(value_source)
            return Q(**dict(((value_lookup + "__in", []),)))

        result = union[0]

        for index in range(1, len(union)):
            result = result | union[index]

        return result

    def get_model_field(self, path):

        model = self.model_class
        parts = path.split('__')

        try:

            for part in parts:

                field = model._meta.get_field(part) # noqa

                if field.is_relation:
                    model = field.related_model
                else:
                    return field

        except exceptions.FieldDoesNotExist:
            return None

    def create_queryset(self):
        return self.model_class.objects.all()

    # noinspection PyMethodMayBeStatic
    def __convert_dotted_path_to_lookup(self, dotted_path):
        return '__'.join(dotted_path.split('.'))

    # noinspection PyMethodMayBeStatic
    def field_value_lookup_from_value_source(self, value_source):

        if isinstance(value_source, PathValueSource):
            return self.__convert_dotted_path_to_lookup(value_source.path)

        raise UnsupportedValueSource

    # noinspection PyMethodMayBeStatic
    def field_label_lookup_from_value_source(self, value_source):

        if isinstance(value_source, PathValueSource):
            return self.__convert_dotted_path_to_lookup(value_source.label_path)

        raise UnsupportedValueSource

    """
    def select_values_from(self, value_source, include_labels=False, limit=None):

        value_lookup = self.field_value_lookup_from_value_source(value_source)
        field = self.get_model_field(value_lookup)

        if field is None:
            return []

        choices = getattr(field, 'choices', None) if field else None

        if choices is not None:

            if not include_labels:
                return [value for value, label in choices]

            return choices

        queryset = self.create_queryset().values_list(field, flat=True).distinct().order_by(field)

        if not include_labels:
            return queryset

        result = [(value, force_str(value)) for value in queryset]
        return self.__map_value_choices(value_source, result, include_labels)
    """

    def select_frequent_values_from(self, value_source, queryset=None, include_labels=False, limit=None):

        # if value_source.value_type is not IntegerType:
        #    return self.__continuous_values_by_frequency(value_source, include_labels, limit)

        if queryset is None:
            queryset = self.create_queryset()

        result = self.__discrete_values_by_frequency(value_source, queryset, include_labels, limit)
        return self.__map_value_choices(value_source, result, include_labels)

    def __map_value_choices(self, value_source, value_choices, include_labels):

        value_lookup = self.field_value_lookup_from_value_source(value_source)

        value_map = self.value_maps.get(value_lookup, None)

        if value_map is None:
            value_map = ValueIdentifierMap()
            self.value_maps[value_lookup] = value_map

        for element in value_choices:

            if include_labels:
                frequency, value, label = element
            else:
                frequency, value = element
                label = force_str(value)

            form_value = value_source.value_type.pack(value)
            identifier = value_map.value_to_identifier(form_value)

            yield QueryEngine.Value(
                    identifier=identifier, form_value=form_value,
                    value=value, frequency=frequency, label=label)

    def __discrete_values_by_frequency(self, value_source, queryset, include_labels, limit):

        value_lookup = self.field_value_lookup_from_value_source(value_source)

        values_list = []
        # values_dict = {'value': Concat(F('name_index__given_names_and_initials'), V(' '), F(value_lookup), output_field=CharField())}
        values_dict = {'value': F(value_lookup)}

        if include_labels:
            label_lookup = self.field_label_lookup_from_value_source(value_source)
            # values_dict['label'] = Concat(F('name_index__given_names_and_initials'), V(' '), F(value_lookup), output_field=CharField())
            values_dict['label'] = Cast(F(label_lookup), output_field=CharField())

        annotations = {
            'frequency': Count('value')
        }

        result = queryset.values(*values_list, **values_dict).filter(
                    value__isnull=False).distinct(). \
            annotate(**annotations).order_by('-frequency', 'value')

        if limit is not None:
            result = result[:limit]

        values_list = ['frequency', 'value']

        if include_labels:
            values_list.append('label')

        result = result.values_list(*values_list)

        return result

    """
    def __continuous_values_by_frequency(self, value_source, include_labels, limit):

        values = self.select_values_from(value_source, include_labels=include_labels)

        path = self.path_from_value_source(value_source)

        # {path + suffix:  for index, suffix in enumerate(('__gte', '__lte'))}

        # When(Q(**{path + '__gte': start, path + '__lt': end}), then=value)
        return []
    """


def resolve_model_string(model_string, default_app=None):
    """
    Resolve an 'app_label.model_name' string into an actual model class.
    If a model class is passed in, just return that.

    Raises a LookupError if a model can not be found, or ValueError if passed
    something that is neither a model or a string.
    """
    if isinstance(model_string, str):
        try:
            app_label, model_name = model_string.split(".")
        except ValueError:
            if default_app is not None:
                # If we can't split, assume a model in current app
                app_label = default_app
                model_name = model_string
            else:
                raise ValueError(
                    "Can not resolve {0!r} into a model. Model names "
                    "should be in the form app_label.model_name".format(model_string),
                    model_string,
                )

        return apps.get_model(app_label, model_name)

    elif isinstance(model_string, type) and issubclass(model_string, Model):
        return model_string

    else:
        raise ValueError(
            "Can not resolve {0!r} into a model".format(model_string), model_string
        )
