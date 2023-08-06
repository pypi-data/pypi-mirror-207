import collections
import importlib

from django.conf import settings
from django.db.models import Q
from django.utils.functional import cached_property

from wagtail import blocks
from wagtail.coreutils import resolve_model_string

from wagtail_switch_block import SwitchBlock
from wagtail_content_block.blocks import ContentProviderBlockMixin, Content, ContentContributorBlockMixin

from .base import QueryHandler
from .apps import get_app_config

__all__ = ['QueryLookupBlock', 'QueryFilterBlock', 'QueryMatchBlock', 'ModelQueryBlock',
           'ContentWithForm', 'AbstractQueryRequestBlockMixin',
           'ImportHandlerQueryRequestBlockMixin', 'ImportHandlerQueryRequestBlock',
           'ModelQueryRequestBlockMixin', 'ModelQueryRequestBlock',
           'QueryRenderBlockMixin',
           'ModelQueryBlock']

APP_CONFIG = get_app_config()

QueryLookup = collections.namedtuple("Lookup", field_names=["identifier", "label"])

EXACT = QueryLookup('exact', 'Exact')
IEXACT = QueryLookup('iexact', 'Exact (Case-Insensitive)')
CONTAINS = QueryLookup('contains', 'Contains')
ICONTAINS = QueryLookup('icontains', 'Contains (Case-Insensitive)')
STARTSWITH = QueryLookup('startswith', 'Starts With')
ISTARTSWITH = QueryLookup('istartswith', 'Starts With (Case-Insensitive)')
ENDSWITH = QueryLookup('endswith', 'Ends With')
IENDSWITH = QueryLookup('iendswith', 'Ends With (Case-Insensitive)')

GREATERTHAN = QueryLookup('gt', 'Greater Than')
GREATERTHANOREQUAL = QueryLookup('gte', 'Greater Than Or Equal')
LESSTHAN = QueryLookup('gt', 'Less Than')
LESSTHANOREQUAL = QueryLookup('gte', 'Less Than Or Equal')

RANGE = QueryLookup('range', 'In Between')
ISNULL = QueryLookup('isnull', 'Check For Null Value')
INLIST = QueryLookup('in', 'Exact (List)')


class QueryLookupBlock(blocks.StructBlock):

    class Meta:
        query_lookup = EXACT

    def __init__(self, **kwargs):

        meta = self._meta_class() # noqa

        query_lookup = kwargs.pop('query_lookup', meta.query_lookup) # noqa
        super().__init__(label=query_lookup.label, query_lookup=query_lookup,**kwargs)

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class QueryMatchBlock(SwitchBlock):

    class Meta:
        default_block_name = 'exact'

    VALUE_KWARGS = {
        'required': False,
        'default': ''
    }

    exact = QueryLookupBlock(query_lookup=EXACT, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    iexact = QueryLookupBlock(query_lookup=IEXACT, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    contains = QueryLookupBlock(query_lookup=CONTAINS, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    icontains = QueryLookupBlock(query_lookup=ICONTAINS, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    startswith = QueryLookupBlock(query_lookup=STARTSWITH, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    istartswith = QueryLookupBlock(query_lookup=ISTARTSWITH, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    endswith = QueryLookupBlock(query_lookup=ENDSWITH, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    iendswith = QueryLookupBlock(query_lookup=IENDSWITH, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])

    greaterthan = QueryLookupBlock(query_lookup=GREATERTHAN, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    greaterthanorequal = QueryLookupBlock(query_lookup=GREATERTHANOREQUAL, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    lessthan = QueryLookupBlock(query_lookup=LESSTHAN, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])
    lessthanorequal = QueryLookupBlock(query_lookup=LESSTHANOREQUAL, local_blocks=[('value', blocks.CharBlock(**VALUE_KWARGS))])

    range = QueryLookupBlock(query_lookup=RANGE, local_blocks=[('min', blocks.CharBlock(**VALUE_KWARGS)), ('max', blocks.CharBlock(**VALUE_KWARGS))])
    isnull = QueryLookupBlock(query_lookup=ISNULL, local_blocks=[('value', blocks.BooleanBlock(default=False, required=False))])
    inlist = QueryLookupBlock(query_lookup=INLIST, local_blocks=[('value', blocks.ListBlock(blocks.CharBlock(**VALUE_KWARGS), default=[]))])


class QueryFilterBlock(blocks.StructBlock):

    class Meta:
        field_choices = []

    def __init__(self, **kwargs):

        meta = self._meta_class() # noqa

        field_choices = kwargs.pop("field_choices", meta.field_choices)
        kwargs.pop("local_blocks", [])

        local_blocks = [
            ('field', blocks.ChoiceBlock(choices=field_choices)),
            ('match', QueryMatchBlock())
        ]

        super().__init__(local_blocks=local_blocks, field_choices=field_choices, **kwargs)

    def deconstruct(self):
        return blocks.Block.deconstruct(self)

    # noinspection PyMethodMayBeStatic
    def define_django_filter(self, value):

        field = value['field']

        match_lookup = value['match'].value.block.meta.query_lookup
        match_value = value['match'].value

        if match_lookup is RANGE:

            match_value = (match_value['min'], match_value['max'])
        else:
            match_value = match_value['value']

            if isinstance(value['match'].value.bound_blocks['value'].block, blocks.ListBlock):
                match_value = list(match_value)

        return field, field + "__" + match_lookup.identifier, match_value


class ModelQueryBlock(ContentProviderBlockMixin, blocks.StructBlock):

    class Meta:
        target_model = None
        field_choices = None

    @cached_property
    def model_class(self):
        return resolve_model_string(self.meta.target_model) # noqa

    def __init__(self, **kwargs):

        meta = self._meta_class() # noqa

        field_choices = kwargs.pop("field_choices", meta.field_choices) # noqa
        kwargs.pop("local_blocks", [])

        local_blocks = [
            ('filters', blocks.ListBlock(QueryFilterBlock(field_choices=field_choices)))
        ]

        super().__init__(local_blocks=local_blocks, field_choices=field_choices, **kwargs)

    def run_query(self, value):

        filters = {}

        for filter_value in value['filters']:

            field_name, field_expr, value = filter_value.block.define_django_filter(filter_value)

            entries = filters.setdefault(field_name, [])
            entries.append((field_expr, value))

        filter_list = []

        for field_name in filters.keys():
            field_filters = filters[field_name]
            field_filters = [Q((field_expr, value)) for field_expr, value in field_filters]

            if len(field_filters) > 1:

                tmp = field_filters[0]

                for field_filter in field_filters[1:]:
                    tmp = tmp | field_filter

                field_filters = tmp
            else:
                field_filters = field_filters[0]

            filter_list.append(field_filters)

        queryset = self.model_class.objects.all().filter(*filter_list)
        return queryset

    def derive_content(self, value, request=None):

        items = self.run_query(value)
        annotations = self.clean_annotations(items)

        return self.create_content(items=items, annotations=annotations)


ContentWithFormDefaults = list(Content._field_defaults) + [None, None] # noqa

ContentWithForm = collections.namedtuple('ContentWithForm',
                                         field_names=list(Content._fields) + ['form', 'result_slice'],
                                         defaults=ContentWithFormDefaults)


class AbstractQueryRequestBlockMixin(ContentProviderBlockMixin):

    class Meta:
        content_class = ContentWithForm
        query_form_classname = settings.QUERYKIT_QUERY_FORM_CLASSNAME
        slice_size = 25

    query_handler = None

    def handle_request(self, request):

        data, files = request.POST if request.method == 'POST' else request.GET, request.FILES
        query = self.query_handler.query_from_form(data, files)
        return query

    def wrap_queryset(self, queryset):

        items = queryset if queryset is not None else []
        annotations = self.clean_annotations(items)

        return self.create_content(items=items, annotations=annotations)

    def form_from_query(self, value, query, request, **kwargs):
        form = self.query_handler.form_from_query(query, url=request.path, **kwargs)
        form.classname = self.meta.query_form_classname # noqa
        return form

    def derive_content_impl(self, value, request=None, queryset=None):

        if request is None:
            return self.wrap_queryset(queryset)

        query = self.handle_request(request)

        if not query.is_valid:
            return self.wrap_queryset(queryset)

        result_slice = query.execute(slice_size=self.meta.slice_size, queryset=queryset) # noqa

        items = list(result_slice.object_list)

        annotations = self.clean_annotations(items)
        form = self.form_from_query(value, query, request, queryset=queryset)

        return self.create_content(items=items, annotations=annotations, form=form, result_slice=result_slice)

    def derive_content(self, value, request=None):
        return self.derive_content_impl(value, request=request)


class ImportHandlerQueryRequestBlockMixin(AbstractQueryRequestBlockMixin):

    class Meta:
        query_handler_import_path = ""

    @cached_property
    def query_handler_module(self):
        parts = self.meta.query_handler_import_path.rsplit('.', maxsplit=1) # noqa

        if len(parts) == 2:
            return parts[0]

        return None

    @cached_property
    def query_handler_name(self):
        parts = self.meta.query_handler_import_path.rsplit('.', maxsplit=1) # noqa

        if len(parts) == 2:
            return parts[1]

        else:
            return parts[0]

    @cached_property
    def query_handler(self):

        if self.query_handler_module:
            module = importlib.import_module(self.query_handler_module)
        else:
            import builtins as module

        return getattr(module, self.query_handler_name, None)


class ImportHandlerQueryRequestBlock(ImportHandlerQueryRequestBlockMixin, blocks.StructBlock):

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class ModelQueryRequestBlockMixin(AbstractQueryRequestBlockMixin):

    class Meta:
        target_model = None

        query_handler_identifier = None
        query_parameters = []
        query_form_widgets = ["clear", "submit"]
        query_form_panels = []

    @cached_property
    def query_handler(self):

        from .django import DjangoQueryEngine

        result = QueryHandler(
            identifier=self.meta.query_handler_identifier or self.meta.target_model, # noqa
            engine=DjangoQueryEngine(target_model=self.meta.target_model), # noqa
            parameters=list(self.meta.query_parameters), # noqa
            widgets=list(self.meta.query_form_widgets), # noqa
            panels=list(self.meta.query_form_panels) # noqa
        )

        return result


class ModelQueryRequestBlock(ModelQueryRequestBlockMixin, blocks.StructBlock):

    fragment_identifier = blocks.CharBlock(required=False, default='')
    panel_layout = blocks.MultipleChoiceBlock(choices=[("compact", "Compact"), ("wide", "Wide")], default="wide")

    def form_from_query(self, value, query, request, **kwargs):
        kwargs['fragment_identifier'] = value['fragment_identifier']
        panel_layout = value['panel_layout']

        if isinstance(panel_layout, str):
            panel_layout = [panel_layout]

        kwargs['panel_layout'] = panel_layout
        return super(ModelQueryRequestBlock, self).form_from_query(value, query, request, **kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class QueryRenderBlockMixin(ContentContributorBlockMixin):

    class Meta:
        content_class = ContentWithForm
        query_form_classname = settings.QUERYKIT_QUERY_FORM_CLASSNAME
        query_form_var = 'form'
        query_result_slice_var = 'result_slice'

    def contribute_content_to_context(self, value, content, context):

        super(QueryRenderBlockMixin, self).contribute_content_to_context(value, content, context) # noqa

        if not isinstance(content, ContentWithForm):
            # This is not query-derived content!
            return

        if self.meta.query_form_var: # noqa
            context[self.meta.query_form_var] = content.form # noqa

        if self.meta.query_result_slice_var: # noqa
            context[self.meta.query_result_slice_var] = content.result_slice # noqa
