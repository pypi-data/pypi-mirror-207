import collections
import copy
import importlib

from django.utils.functional import cached_property
from django.utils.deconstruct import deconstructible
from django.utils.datastructures import MultiValueDict

from django_auxiliaries.variable_scope import load_variable_scope

# from steadfast import *

from .apps import get_app_label
from .forms import QueryForm, FormPanel, Choice
from .value_types import CharType, IntegerType
from .value_sources import ValueSource
from .utilities import construct

__all__ = [
    'SliceNumberNotNumeric', 'SliceNumberOutOfRange',
    'QueryResultSlice', 'QueryResult',
    'Descriptor', 'LabelMixin',
    'QuerySetting', 'Query',
    'QueryParameter', 'QueryExecution',
    'QueryEngine', 'QueryHandler',
    'Filter', 'ResultSliceParameter',
    'OrderSpecifier', 'OrderParameter', 'SliceSizeParameter'
]

APP_LABEL = get_app_label()


class SliceNumberNotNumeric(RuntimeError):
    pass


class SliceNumberOutOfRange(RuntimeError):
    pass


class QueryResultSlice:

    """Returned by :func:`QueryResult.slice_for_number` .

    Holds a contiguous subset of objects retrieved by a :class:`Query`.
    """

    @property
    def result(self):
        """The :class:`QueryResult` this slice belongs to.
        """
        return None

    @property
    def object_list(self):
        """A sub-sequence of objects retrieved by the underlying :class:`Query`.
        """
        return []

    @property
    def number(self):
        """The 1-based number of this slice.
        """
        return 1

    @property
    def is_first(self):
        """Is this the first slice of its :class:`QueryResult`?
        """
        return True

    @property
    def is_last(self):
        """Is this the last slice of its :class:`QueryResult`?
        """
        return True

    @property
    def is_only_slice(self):
        """Is this the only slice of its :class:`QueryResult`?
        """
        return True

    @property
    def is_empty(self):
        """Does this slice hold any objects?
        """
        return True

    @property
    def slice_object_count(self):
        """The number of objects in this :class:`QueryResultSlice`.
        """
        return 0

    @property
    def first_object_index(self):
        """The 1-based index of the first object in this slice, out of all objects in the :class:`QueryResult`.
        """
        return 1

    @property
    def last_object_index(self):
        """The 1-based index of the last object in this slice, out of all objects in the :class:`QueryResult`.

        Only valid if is_empty() is False.
        """
        return 1

    @property
    def object_index_range(self):
        return range(self.first_object_index, self.last_object_index + 1)


class QueryResult:

    """Returned by :func:`Query.execute`.

    Holds the objects retrieved by a :class:`Query`.
    """

    @property
    def query(self):
        return None

    @property
    def object_list(self):
        """The sequence of objects retrieved by a :class:`Query`.
        """
        return []

    @property
    def total_object_count(self):
        """The total number of objects retrieved by a :class:`Query`.
        """
        return 0

    @property
    def total_slice_count(self):
        """The total number of :class:`QueryResultSlice` s in this result.
        """
        return 0

    @property
    def slice_number_range(self):
        """A list of :class:`QueryResultSlice` numbers.
        """
        return []

    @property
    def slice_size(self):
        """The standard number of objects per :class:`QueryResultSlice`.
        """
        return 10

    def slice_for_number(self, number):
        """Retrieve the :class:`QueryResultSlice` with a given number.

        :param number: A 1-based slice number
        :return: A corresponding :class:`QueryResultSlice` instance.
        """

        if number < 1:
            raise SliceNumberOutOfRange

        if number > 1:
            raise SliceNumberOutOfRange

        return QueryResultSlice()


@deconstructible
class Descriptor:

    @property
    def identifier(self):
        return self._identifier

    def __init__(self, *, identifier, **kwargs):
        self._identifier = identifier

        super(Descriptor, self).__init__(**kwargs)


@deconstructible
class LabelMixin:

    @property
    def label(self):
        return self._label

    def __init__(self, *, label='', **kwargs):

        super(LabelMixin, self).__init__(**kwargs)

        if not label:
            label = getattr(self, 'identifier', '').replace('_', ' ').capitalize()

        self._label = label


class QuerySetting(LabelMixin, Descriptor):

    """A setting as applied in an instance of :class:`Query`.

    """

    @property
    def parameter(self):
        """
        The :class:`QueryParameter` object that created this setting.
        """
        return self._parameter

    @property
    def value_list(self):
        """
        The value list defined for this setting.
        """
        return self._value_list[:]

    def __init__(self, *, parameter, value_list, **kwargs):
        super(QuerySetting, self).__init__(**kwargs)

        if value_list is None:
            value_list = []

        self._parameter = parameter
        self._value_list = list(value_list)


class Query:

    """A reusable instance of a query.

    A query holds a number of filters.
    """

    @property
    def handler(self):
        """
        The :class:`QueryHandler` object that created this query.
        """
        return self._handler

    @property
    def engine(self):
        """
        A shortcut via the handler to :class:`QueryEngine` object underlying this query.
        """
        return self._handler

    @property
    def settings_map(self):
        """
        A mapping from identifiers to :class:`QuerySetting` s
        """
        return dict(self._settings)

    @property
    def settings(self):
        """
        An iterator over all :class:`QuerySetting` objects defined in this query.
        """
        return self._settings.values()

    @cached_property
    def result_slice_identifier(self):

        if self._result_slice_identifier is None:

            for identifier, setting in self._settings.items():
                if isinstance(setting.parameter, ResultSliceParameter):
                    self._result_slice_identifier = identifier
                    break

        return self._result_slice_identifier

    @cached_property
    def slice_size_identifier(self):

        if self._slice_size_identifier is None:

            for identifier, setting in self._settings.items():
                if isinstance(setting.parameter, SliceSizeParameter):
                    self._slice_size_identifier = identifier
                    break

        return self._slice_size_identifier

    @cached_property
    def order_identifier(self):

        if self._order_identifier is None:

            for identifier, setting in self._settings.items():
                if isinstance(setting.parameter, OrderParameter):
                    self._order_identifier = identifier
                    break

        return self._order_identifier

    @cached_property
    def is_valid(self):
        """
        Indicates if this query is valid by calling validate() as required.
        """
        return self.validate()

    def __init__(self, *, handler, settings=None, **kwargs):

        """
        Initialises a new query instance.

        :param handler: The :class:`QueryHandler` that created this object.
        :param settings: An optional list of :class:`QuerySetting` s.

        """

        super(Query, self).__init__(**kwargs)

        if settings is None:
            settings = collections.OrderedDict()

        self._handler = handler
        self._settings = collections.OrderedDict(settings)
        self._result_slice_identifier = None
        self._slice_size_identifier = None
        self._order_identifier = None

        self.__clear_is_valid()

    def add_setting(self, setting):
        self._settings[setting.identifier] = setting
        self.__dict__.pop('result_slice_identifier', None)
        self.__clear_is_valid()

    def __clear_is_valid(self):
        self.__dict__.pop('is_valid', None)

    def url_encode(self, data, prefix='', only=None, filter=None):

        if only is None:
            only = []

        if filter is None:
            filter = []

        for parameter in self.handler.parameters:

            if only and parameter.identifier not in only:
                continue

            if filter and parameter.identifier in filter:
                continue

            identifier = prefixed(parameter.identifier, prefix)
            setting = self.settings_map.get(identifier, None)

            if setting is None:
                continue

            data.setlist(identifier, setting.value_list)

    # noinspection PyMethodMayBeStatic
    def validate(self):
        return True

    # noinspection PyMethodMayBeStatic
    def execute(self, *, slice_size=None, **kwargs) -> QueryResultSlice:
        execution = self.handler.engine.construct_execution_for(query=self, slice_size=slice_size, **kwargs)
        return execution.run()

    def copy(self):
        return copy.copy(self)


def prefixed(identifier, prefix=''):
    return "%s-%s" % (prefix, identifier) if prefix else identifier


@deconstructible
class QueryParameter(Descriptor):

    def __init__(self, **kwargs):
        super(QueryParameter, self).__init__(**kwargs)

    # noinspection PyMethodMayBeStatic
    def initialise_from_form_data(self, query, data, files, prefix=''):
        pass

    # noinspection PyMethodMayBeStatic
    def contribute_to_form(self, query, form, queryset=None, prefix=''):
        pass


class QueryExecution:

    # noinspection PyMethodMayBeStatic
    def run(self) -> QueryResultSlice:
        return QueryResultSlice()


class QueryEngine:

    """A factory for common implementation-specific objects used by :class:`QueryHandler` and other classes.

    """

    Value = collections.namedtuple('Value', field_names=['identifier', 'form_value', 'value', 'label', 'frequency'])

    # noinspection PyMethodMayBeStatic
    def construct_execution_for(self, *, query, **kwargs):
        raise NotImplementedError("construct_execution_for() must be implemented by subclasses")

    """
    def select_values_from(self, value_source, include_labels=False, limit=None):
        raise NotImplementedError("select_values_from() must be implemented by subclasses")
    """

    def select_frequent_values_from(self, value_source, queryset=None, include_labels=False, limit=None):
        raise NotImplementedError("select_frequent_values_from() must be implemented by subclasses")


class QueryHandler(LabelMixin, Descriptor):

    """Performs all query-related operations associated with a particular domain or model.

    A handler defines, executes and renders queries on the basis of the filter categories defined
    for it.

    """

    ParameterEntry = collections.namedtuple("ParameterEntry", field_names=["parameter", "handler"])

    @property
    def engine(self):
        """
        The :class:`QueryEngine` object that handles implementation-specific functions for this handler.
        """
        return self._engine

    @property
    def parameter_map(self):
        """
        A mapping from identifiers to :class:`ParameterEntry` s
        """
        return dict(self._parameter_entries)

    @property
    def parameters(self):
        """
        An iterator over all :class:`QueryParameter` s registered with this handler.
        """

        for entry in self._parameter_entries.values():
            yield entry.parameter

    @property
    def widgets(self):
        return self._widgets[:]

    @property
    def panels(self):
        return self._panels[:]

    def __init__(self, *, engine, parameters=None, widgets=None, panels=None, **kwargs):
        super(QueryHandler, self).__init__(**kwargs)

        if parameters is None:
            parameters = []

        if widgets is None:
            widgets = []

        if panels is None:
            panels = []

        self._engine = engine
        self._parameter_entries = self._construct_parameter_entries(parameters)
        self._widgets = list(widgets)
        self._panels = list(panels)

    def _construct_parameter_entries(self, parameters):

        result = {}

        for parameter in parameters:

            # handler = self.engine.construct_filter_handler(category.value_type)
            entry = self.ParameterEntry(parameter=parameter, handler=None)
            result[parameter.identifier] = entry

        return result

    def query_from_form(self, data, files, prefix=''):
        """Creates a :class:`Query` object from the data and file dictionaries obtained from a HTTP request.

        :param data: A MultiDict of submitted query parameters
        :param files: A MultiDict of submitted files
        :param prefix: An (optional) prefix to identify query parameters
        :return: A new :class:`Query` instance
        """

        # q = self.engine.construct_query(self)
        q = Query(handler=self)

        for parameter in self.parameters:
            parameter.initialise_from_form_data(q, data, files, prefix=prefix)

        return q

    # noinspection PyMethodMayBeStatic
    def form_from_query(self, query, url, prefix='', fragment_identifier='', panel_layout='', queryset=None):

        form = QueryForm()

        scope = load_variable_scope(APP_LABEL, query_index=0)
        scope.query_index += 1

        form.identifier = 'query-' + '{:d}'.format(scope.query_index)
        form.fragment_identifier = fragment_identifier
        form.panel_layout = panel_layout
        form.url = url

        standard = []

        if query.result_slice_identifier:
            standard.append(query.result_slice_identifier)

        if query.slice_size_identifier:
            standard.append(query.slice_size_identifier)

        if query.order_identifier:
            standard.append(query.order_identifier)

        query.url_encode(form.url_encoded_data, prefix, only=standard)

        form.add_common_widgets(self.widgets)

        query.url_encode(form.url_encoded_data, prefix, filter=standard)

        for parameter in self.parameters:
            parameter.contribute_to_form(query, form, queryset=queryset, prefix=prefix)

        panels = self.panels

        if not panels:
            panels = ['*']

        expanded_panels = []

        for panel in panels:
            if panel == '*':
                expanded_panels.extend(form.widgets_by_category.keys())

                if QueryForm.APPLIED_FILTERS_CATEGORY not in expanded_panels:
                    # Make sure the applied filters panel is shown even if no filters are applied.
                    expanded_panels.append(QueryForm.APPLIED_FILTERS_CATEGORY)

                continue

            expanded_panels.append(panel)

        for panel in expanded_panels:

            if isinstance(panel, str):
                panel = FormPanel(identifier=panel, widget_categories=(panel,))
            else:
                path, args, kwargs = panel.deconstruct()
                panel = construct(path, args, kwargs)

            if not panel.html_identifier:
                panel.html_identifier = form.identifier + "-" + panel.identifier

            if not panel.classname:
                panel.classname = "query-panel" + " query-panel-" + panel.identifier.replace('_', '-').lower()

            form.add_panel(panel)

        form.assign_widgets_to_panels()

        return form

    # noinspection PyMethodMayBeStatic
    def build_slice_number_urls_for_result(self, form, result, slice_numbers, prefix=''):

        urls = []
        result_slice_identifier = result.query.result_slice_identifier

        if result_slice_identifier:

            for slice_number in slice_numbers:
                query = result.query.copy()
                result_slice_setting = query.settings_map[result_slice_identifier]

                result_slice_setting = QuerySetting(identifier=result_slice_identifier,
                                                    parameter=result_slice_setting.parameter,
                                                    value_list=[slice_number])

                query.add_setting(result_slice_setting)

                data = MultiValueDict()
                query.url_encode(data, prefix)
                urls.append(form.url_with_data(data))

        return urls


class Filter(LabelMixin, QueryParameter):

    """A category of filters understood by a :class:`QueryHandler`.

    A filter category specifies a :class:`ValueType`.
    """

    @property
    def value_source(self):
        """
        The :class:`ValueSource` underlying this filter.
        """
        return self._value_source

    @property
    def widget_factory(self):
        """
        The :class:`FormWidgetFactory` used by this filter.
        """
        return self._widget_factory

    def __init__(self, *, value_source=None, widget_factory, **kwargs):
        super(Filter, self).__init__(**kwargs)

        if value_source is None:
            value_source = ValueSource(value_type=CharType)

        self._value_source = value_source
        self._widget_factory = widget_factory

    # noinspection PyMethodMayBeStatic
    def initialise_from_form_data(self, query, data, files, prefix=''):
        identifier = prefixed(self.identifier, prefix)
        value_type = self.value_source.value_type

        values = self._widget_factory.values_from_form(identifier, value_type, data, files)

        setting = QuerySetting(parameter=self, identifier=self.identifier, value_list=values)
        query.add_setting(setting)

    def contribute_to_form(self, query, form, queryset=None, prefix=''):

        widgets = self._widget_factory(parameter=self, value_source=self.value_source, query=query, form=form,
                                       queryset=queryset, prefix=prefix)

        for widget in widgets:
            form.add_widget(widget)


class ResultSliceParameter(LabelMixin, QueryParameter):

    """A category of filters understood by a :class:`QueryHandler`.

    A filter category specifies a :class:`ValueType`.
    """

    @property
    def widget_factory(self):
        """
        The :class:`FormWidgetFactory` used by this filter.
        """
        return self._widget_factory

    def __init__(self, *, widget_factory, **kwargs):
        super(ResultSliceParameter, self).__init__(**kwargs)

        self._widget_factory = widget_factory

    # noinspection PyMethodMayBeStatic
    def initialise_from_form_data(self, query, data, files, prefix=''):
        identifier = prefixed(self.identifier, prefix)
        value_type = IntegerType
        values = [value_type.unpack(value) for value in data.getlist(identifier, []) if value]

        if values and len(values) > 1:
            values = [values[0]]

        setting = QuerySetting(parameter=self, identifier=self.identifier, value_list=values)
        query.add_setting(setting)

    def contribute_to_form(self, query, form, queryset=None, prefix=''):
        pass


class OrderSpecifier:

    @property
    def identifier(self):
        return self._identifier

    @property
    def label(self):
        return self._label

    @property
    def value_sources(self):
        return self._value_sources[:]

    def __init__(self, identifier, label, *value_sources):
        self._identifier = identifier
        self._label = label
        self._value_sources = value_sources


class OrderParameter(LabelMixin, QueryParameter):

    @property
    def widget_factory(self):
        """
        The :class:`FormWidgetFactory` used by this filter.
        """
        return self._widget_factory

    @property
    def order_specifier_map(self):
        return self._order_specifier_map

    @property
    def choices_for_widget(self):
        return [Choice(order.identifier, order.label) for order in self._order_specifiers]

    def __init__(self, *, widget_factory, order_specifiers=None, default_choice=None, user_editable=True, **kwargs):
        super(OrderParameter, self).__init__(**kwargs)

        if order_specifiers is None:
            order_specifiers = []

        if default_choice is None and order_specifiers:
            default_choice = order_specifiers[0].identifier

        from .forms import SelectFactory

        self._widget_factory = widget_factory or SelectFactory()
        self._order_specifiers = list(order_specifiers)
        self._default_choice = default_choice
        self._user_editable = user_editable

        self.__update_order_specifier_map()

    def __update_order_specifier_map(self):
        self._order_specifier_map = {order.identifier: order for order in self._order_specifiers}

    # noinspection PyMethodMayBeStatic
    def initialise_from_form_data(self, query, data, files, prefix=''):

        identifier = prefixed(self.identifier, prefix)
        value_type = CharType

        values = self._widget_factory.values_from_form(identifier, value_type, data, files)

        if values and len(values) > 1:
            values = [values[0]]

        if not values and self._default_choice:
            values = [self._default_choice]

        setting = QuerySetting(parameter=self, identifier=self.identifier, value_list=values)
        query.add_setting(setting)

    def contribute_to_form(self, query, form, queryset=None, prefix=''):

        widgets = self._widget_factory(parameter=self, query=query, form=form,
                                       queryset=queryset, prefix=prefix, choices=self.choices_for_widget)

        for widget in widgets:
            form.add_widget(widget)


class SliceSizeParameter(LabelMixin, QueryParameter):

    @property
    def widget_factory(self):
        """
        The :class:`FormWidgetFactory` used by this filter.
        """
        return self._widget_factory

    @property
    def size_choices(self):
        return self._size_choices

    def __init__(self, *, widget_factory, size_choices=None, default_choice=None, user_editable=True, **kwargs):
        super(SliceSizeParameter, self).__init__(**kwargs)

        if size_choices is None:
            size_choices = []

        if default_choice is None and size_choices:
            default_choice = size_choices[0][0]

        self._widget_factory = widget_factory
        self._size_choices = list(size_choices)
        self._default_choice = default_choice
        self._user_editable = user_editable

    # noinspection PyMethodMayBeStatic
    def initialise_from_form_data(self, query, data, files, prefix=''):

        identifier = prefixed(self.identifier, prefix)
        value_type = CharType

        values = self._widget_factory.values_from_form(identifier, value_type, data, files)

        if values and len(values) > 1:
            values = [values[0]]

        if not values and self._default_choice:
            values = [self._default_choice]

        if values:
            try:
                values[0] = int(values[0])
            except ValueError:
                pass

        setting = QuerySetting(parameter=self, identifier=self.identifier, value_list=values)
        query.add_setting(setting)

    def contribute_to_form(self, query, form, queryset=None, prefix=''):

        widgets = self._widget_factory(parameter=self, query=query, form=form,
                                       queryset=queryset, prefix=prefix, choices=self.size_choices)

        for widget in widgets:
            form.add_widget(widget)
