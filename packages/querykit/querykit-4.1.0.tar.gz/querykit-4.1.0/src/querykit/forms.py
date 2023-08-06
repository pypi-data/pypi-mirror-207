import bisect

from collections import namedtuple
from urllib.parse import urlencode


from django.template.loader import render_to_string
from django.utils.deconstruct import deconstructible
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDict
from django.utils.functional import cached_property

from .apps import get_app_label
from .utilities import construct

__all__ = ['QueryForm', 'FormPanel', 'CompositeFormPanel', 'ResultRangePanel',
           'FormWidgetFactory', 'FormWidget', 'FormWidgetLiteral', 'PickerFactory', 'SelectFactory',
           'Choice', 'Button']

APP_LABEL = get_app_label()


class WidgetRegistry:

    @property
    def widgets(self):
        return self._widgets.values()

    @cached_property
    def ordered_widgets(self):
        return sorted(self.widgets, key=lambda w: (w.category, w.category_order))

    @property
    def widgets_by_category(self):
        return self._widgets_by_category

    @property
    def ordered_widgets_by_category(self):
        return self._ordered_widgets_by_category

    def __init__(self):

        self._widgets = {}
        self._widgets_by_category = {}
        self._ordered_widgets_by_category = {}

    def filter_widgets_by_category(self, *categories):

        for category in categories:
            widgets = self._widgets_by_category.get(category, None)

            if widgets is None:
                continue

            for widget in widgets:
                yield widget

    def add_widget(self, widget):

        self._widgets[widget.identifier] = widget

        widgets = self._widgets_by_category.setdefault(widget.category, [])
        widgets.append(widget)

        widgets = self._ordered_widgets_by_category.setdefault(widget.category, [])
        index = bisect.bisect([widget.category_order for widget in widgets], widget.category_order)
        widgets.insert(index, widget)

        self.__dict__.pop('ordered_widgets', None)


class PanelRegistry:

    @property
    def panels(self):
        return self._panels.values()

    @property
    def panel_identifiers(self):
        return self._panels.keys()

    @property
    def panels_by_identifier(self):
        return self._panels

    @property
    def ordered_panels(self):
        return self._panels.values()

    @property
    def ordered_panel_identifiers(self):
        return self._panels.keys()

    def __init__(self):

        self._panels = {}
        self._panels_by_category = {}

    def add_panel(self, panel):

        previous_panel = self._panels.get(panel.identifier, None)

        if previous_panel:

            del self._panels[panel.identifier]

            for category in previous_panel.widget_categories:
                panels = self._panels_by_category.get(category, [])

                try:
                    index = panels.index(previous_panel)
                    panels.pop(index)

                    if not panels:
                        del self._panels_by_category[category]

                except ValueError:
                    pass

        self._panels[panel.identifier] = panel

        for category in panel.widget_categories:
            panels = self._panels_by_category.setdefault(category, [])
            panels.append(panel)

        return panel

    def assign_widgets(self, widgets_by_category):

        for category, widgets in widgets_by_category.items():

            panels = self._panels_by_category.get(category, [])

            for panel in panels:
                for widget in widgets:
                    panel.add_widget(widget)


@deconstructible
class FormPanel(WidgetRegistry):

    @property
    def identifier(self):
        return self._identifier

    @property
    def html_identifier(self):
        return self._html_identifier

    @html_identifier.setter
    def html_identifier(self, value):
        self._html_identifier = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def classname(self):
        return self._classname

    @classname.setter
    def classname(self, value):
        self._classname = value

    @property
    def show_query_panel_label(self):
        return self._show_query_panel_label

    @show_query_panel_label.setter
    def show_query_panel_label(self, value):
        self._show_query_panel_label = value

    @property
    def apply_filters_label(self):
        return self._apply_filters_label

    @apply_filters_label.setter
    def apply_filters_label(self, value):
        self._apply_filters_label = value

    @property
    def requires_widgets_to_render(self):
        return self._requires_widgets_to_render

    @requires_widgets_to_render.setter
    def requires_widgets_to_render(self, value):
        self._requires_widgets_to_render = value

    @property
    def template(self):
        return self._template

    @property
    def widget_categories(self):
        return self._widget_categories[:]

    def __init__(self, *, identifier, widget_categories=None, label=None, classname='', show_query_panel_label='',
                 apply_filters_label='', requires_widgets_to_render=False, template=None):

        super(FormPanel, self).__init__()

        if widget_categories is None:
            widget_categories = []

        if show_query_panel_label is None:
            show_query_panel_label = 'Show Filters'

        if apply_filters_label is None:
            apply_filters_label = 'Apply Filters'

        self._identifier = identifier
        self._html_identifier = ''
        self._label = label if label is not None else identifier.replace('_', ' ').capitalize()
        self._classname = classname
        self._show_query_panel_label = show_query_panel_label
        self._apply_filters_label = apply_filters_label
        self._requires_widgets_to_render = requires_widgets_to_render
        self._template = template if template else APP_LABEL + "/form_panel.html"

        self._widget_categories = list(widget_categories)

    def get_template_context(self, parent_context=None):

        context = {} if not parent_context else dict(parent_context)

        context.update({
            'panel': self,
        })

        return context

    def render(self, context=None):
        context = self.get_template_context(parent_context=context)
        return render_to_string(self.template, context=context)


class CompositeFormPanel(PanelRegistry, FormPanel):

    @cached_property
    def widget_categories(self):

        result = set()

        for panel in self.ordered_panels:
            result.update(panel.widget_categories)

        return list(result)

    def __init__(self, *, identifier, label=None, classname='', template=None, panels=None):

        PanelRegistry.__init__(self)

        template = template if template else APP_LABEL + "/composite_form_panel.html"

        FormPanel.__init__(self,
                           identifier=identifier,
                           widget_categories=[],
                           label=label,
                           classname=classname,
                           template=template)

        if panels is None:
            panels = []

        for panel in panels:
            self.add_panel(panel)

    def deconstruct(self):
        path, args, kwargs = super(CompositeFormPanel, self).deconstruct()

        panels = kwargs.pop('panels', None)
        panels_copy = []

        if panels:
            for panel in panels:
                panel_specifier = panel.deconstruct()
                panels_copy.append(construct(*panel_specifier))

        kwargs['panels'] = panels_copy
        return path, args, kwargs

    def add_panel(self, panel):
        super(CompositeFormPanel, self).add_panel(panel)
        self.__dict__.pop('widget_categories', None)

    def assign_widgets_to_panels(self):
        self.assign_widgets(self.widgets_by_category)

        for panel in self.panels:

            if not panel.html_identifier:
                panel.html_identifier = self.html_identifier + "-" + panel.identifier

            if not panel.classname:
                panel.classname = "query-panel" + " query-panel-" + panel.identifier.replace('_', '-').lower()


class ResultRangePanel(FormPanel):

    @property
    def result_label(self):
        return self._result_label

    @result_label.setter
    def result_label(self, value):
        self._result_label = value

    @property
    def result_label_plural(self):
        return self._result_label_plural

    @result_label_plural.setter
    def result_label_plural(self, value):
        self._result_label_plural = value

    def __init__(self, *, identifier, label=None, classname='', template=None, result_label=None, result_label_plural=None):

        template = template if template else APP_LABEL + "/result_range_panel.html"

        FormPanel.__init__(self,
                           identifier=identifier,
                           widget_categories=[],
                           label=label,
                           classname=classname,
                           template=template)

        self._result_label = result_label
        self._result_label_plural = result_label_plural

    def get_template_context(self, parent_context=None):
        context = super().get_template_context(parent_context=parent_context)

        if not context.get('result_label', ''):
            context['result_label'] = self.result_label

        if not context.get('result_label_plural', ''):
            context['result_label_plural'] = self.result_label_plural

        return context


class QueryForm(WidgetRegistry, PanelRegistry):

    do_not_call_in_templates = True

    template = APP_LABEL + "/query_form.html"

    GENERAL_CATEGORY = 'general'
    FILTERS_CATEGORY = 'filters'
    APPLIED_FILTERS_CATEGORY = 'applied_filters'
    RESULT_RANGE_CATEGORY = 'result_range'

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = value

    @property
    def fragment_identifier(self):
        return self._fragment_identifier if self._fragment_identifier else self._identifier

    @fragment_identifier.setter
    def fragment_identifier(self, value):
        self._fragment_identifier = value

    @property
    def panel_layout(self):
        return self._panel_layout

    @panel_layout.setter
    def panel_layout(self, value):
        self._panel_layout = value

    @property
    def panel_layout_classname(self):
        return " ".join(["query-panel-layout-" + item for item in self._panel_layout])

    @property
    def classname(self):
        return self._classname

    @classname.setter
    def classname(self, value):
        self._classname = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def widget_templates(self):
        return self._widget_templates

    @property
    def ordered_panel_block_definitions(self):
        return {key: '{{% include_query_form_panel form.panels_by_identifier.{} %}}'.format(key) for key in self._panels.keys()}

    @property
    def url_encoded_data(self):
        return self._url_encoded_data

    def __init__(self, template=None):
        super(QueryForm, self).__init__()

        self._identifier = ''
        self._fragment_identifier = ''
        self._panel_layout = ''
        self._classname = ''
        self._method = "get"
        self._url = ""

        self._widget_templates = {}
        self._panels = {}
        self._panels_by_category = {}
        self._url_encoded_data = MultiValueDict()

        self._composite_panels = []

        if template is not None:
            self.template = template

        self._widget_templates['clear'] = \
            Button(identifier="clear", label="Clear", type="reset", alternative_url_type="clear", category_order=1000)

        self._widget_templates['submit'] = \
            Button(identifier="submit", label="Update", type="submit", alternative_url_type="submit", category_order=1001)

    def url_of_type(self, url_type):

        if url_type == 'submit':
            return ''

        if url_type == 'clear':
            return self.url_with_data(self.url_encoded_data)

        return self._url

    def url_with_data(self, data):
        query_params = urlencode(data, doseq=True)
        result = self.url + "?" + query_params + "#" + self.fragment_identifier
        return result

    def add_common_widgets(self, widgets):

        for widget in widgets:

            if isinstance(widget, str):
                widget = self.widget_templates.get(widget, None)

                if widget is None:
                    continue

            path, args, kwargs = widget.deconstruct()

            kwargs['form_id'] = self.identifier

            if 'alternative_url_type' in kwargs:
                alternative_url = self.url_of_type(kwargs['alternative_url_type'])
                kwargs['alternative_url'] = alternative_url

            widget = construct(path, args, kwargs)
            self.add_widget(widget)

    def add_panel(self, panel):
        super(QueryForm, self).add_panel(panel)

        if isinstance(panel, CompositeFormPanel):
            self._composite_panels.append(panel)

    def assign_widgets_to_panels(self):
        self.assign_widgets(self.widgets_by_category)

        for panel in self._composite_panels:
            panel.assign_widgets_to_panels()

    def get_template_context(self):

        context = {
            'form': self,
            'action_url': self.url + "#" + self.identifier
        }

        return context

    def render(self):
        context = self.get_template_context()
        return render_to_string(self.template, context=context)

    def __call__(self):
        return self.render()


@deconstructible
class FormWidget:

    @property
    def category(self):
        return self._category

    @property
    def category_order(self):
        return self._category_order

    @property
    def form_id(self):
        return self._form_id

    def __init__(self, *, category='', category_order=0, form_id=''):

        if not category:
            category = QueryForm.GENERAL_CATEGORY

        self._category = category
        self._category_order = category_order
        self._form_id = form_id

    def render(self):
        return ''


def prefixed(identifier, prefix=''):
    return "%s-%s" % (prefix, identifier) if prefix else identifier


Choice = namedtuple("Choice", field_names=["identifier", "label"])


class FormWidgetFactory:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def values_from_form(self, identifier, value_type, data, files):
        values = [value_type.unpack(value) for value in data.getlist(identifier, []) if value]
        return values

    def __call__(self, *, parameter, query, form, queryset=None, prefix='', **kwargs):
        return None


class FormWidgetLiteral(FormWidget):

    def __init__(self, *, text, category):
        super(FormWidgetLiteral, self).__init__(category=category)
        self.text = text

    def render(self):
        return mark_safe(self.text)


class TemplateWidget(FormWidget):

    template = ''

    def __init__(self, *, template=None, **kwargs):
        super(TemplateWidget, self).__init__(**kwargs)

        if template is not None:
            self.template = template

    def get_template_context(self):

        context = {
            'widget': self
        }

        return context

    def render(self):
        context = self.get_template_context()
        return render_to_string(self.template, context=context)


class Button(TemplateWidget):

    template = APP_LABEL + "/form_widgets/button.html"

    def __init__(self, *, identifier, label, type, alternative_url='', alternative_url_type='', **kwargs):
        super(Button, self).__init__(**kwargs)

        self.identifier = identifier
        self.label = label
        self.type = type
        self.alternative_url = alternative_url

    def get_template_context(self):

        context = super(Button, self).get_template_context()

        context.update({ # noqa
        })

        return context


class Select(TemplateWidget):

    template = APP_LABEL + "/form_widgets/select.html"

    def __init__(self, *, category, identifier, label, choices, initial_choice, allow_multiple_selection, **kwargs):
        super(Select, self).__init__(category=category, **kwargs)

        self.identifier = identifier
        self.label = label
        self.choices = choices
        self.initial_choice = initial_choice
        self.allow_multiple_selection = allow_multiple_selection

    def get_template_context(self):

        context = super(Select, self).get_template_context()

        context.update({ # noqa
            'choices': self.choices,
            'sorted_choices': list(enumerate(sorted(self.choices, key=lambda x: x.label), start=1))
        })

        return context


class SelectFactory(FormWidgetFactory):

    def __init__(self):
        super(SelectFactory, self).__init__()

    # noinspection PyMethodMayBeStatic
    def values_from_form(self, identifier, value_type, data, files):
        values = [value_type.unpack(value) for value in data.getlist(identifier, []) if value]
        return values

    def __call__(self, *, parameter, query, form, queryset=None, prefix='', **kwargs):

        choices = kwargs.pop('choices', [])
        initial_choice = kwargs.pop('initial_choice', None)
        widget_category = kwargs.pop('widget_category', QueryForm.GENERAL_CATEGORY)

        setting = query.settings_map[parameter.identifier]
        identifier = prefixed(parameter.identifier, prefix)

        if setting.value_list:
            initial_choice = setting.value_list[0]

        if initial_choice is None and choices:
            initial_choice = choices[0][0]

        widgets = []

        widget = Select(category=widget_category,
                        identifier=identifier,
                        label=parameter.label,
                        choices=choices,
                        initial_choice=initial_choice,
                        allow_multiple_selection=False,
                        form_id=form.identifier)

        widgets.append(widget)

        return widgets


class Label(TemplateWidget):

    def __init__(self, *, identifier, text, **kwargs):
        super(Label, self).__init__(**kwargs)

        self.identifier = identifier
        self.text = text


class DeletableLabel(Label):

    template = APP_LABEL + "/form_widgets/deletable_label.html"

    def __init__(self, *, category, identifier, text, alternative_url, **kwargs):
        super(DeletableLabel, self).__init__(category=category, identifier=identifier, text=text, **kwargs)

        self.alternative_url = alternative_url


class Picker(TemplateWidget):

    Choice = namedtuple("Choice", field_names=list(Choice._fields) +
                        ["selected", "value", "frequency", "alternative_url"])

    template = APP_LABEL + "/form_widgets/picker.html"

    def __init__(self, *, category, identifier, label, choices, **kwargs):
        super(Picker, self).__init__(category=category, **kwargs)

        self.identifier = identifier
        self.label = label
        self.choices = choices

    def get_template_context(self):

        context = super(Picker, self).get_template_context()

        context.update({ # noqa
            'sorted_choices': list(enumerate(sorted(self.choices, key=lambda x: x.label), start=1))
        })

        return context


class PickerFactory(FormWidgetFactory):

    def __init__(self):
        super(PickerFactory, self).__init__()

    # noinspection PyMethodMayBeStatic
    def values_from_form(self, identifier, value_type, data, files):
        values = [value for value in data.getlist(identifier, []) if value]  # value_type.unpack(value)
        return values

    def __call__(self, *, parameter, query, form, queryset=None, prefix='', **kwargs):

        value_source = kwargs.pop('value_source', None)

        if value_source is None:
            return []

        engine = query.handler.engine

        setting = query.settings_map[parameter.identifier]
        identifier = prefixed(parameter.identifier, prefix)

        selection_list = set(setting.value_list or [])

        frequent_values = engine.select_frequent_values_from(value_source, queryset=queryset,
                                                             include_labels=True, limit=16)

        choices = []
        widgets = []

        for engine_value in frequent_values:

            selected = engine_value.identifier in selection_list

            alternative_url_encoded_data = form.url_encoded_data.copy()

            if selected:
                alternative_list = [value for value in alternative_url_encoded_data.getlist(identifier)
                                    if value != engine_value.identifier]
            else:
                alternative_list = list(alternative_url_encoded_data.getlist(identifier))
                alternative_list.append(engine_value.identifier)

            alternative_url_encoded_data.setlist(identifier, alternative_list)

            if query.result_slice_identifier:
                alternative_url_encoded_data.setlist(query.result_slice_identifier, [1])

            alternative_url = form.url_with_data(list(alternative_url_encoded_data.lists()))

            choice = Picker.Choice(identifier=engine_value.identifier, # noqa
                                   label=engine_value.label, # noqa
                                   value=engine_value.identifier, # noqa
                                   frequency=engine_value.frequency, # noqa
                                   selected=selected, # noqa
                                   alternative_url=alternative_url) # noqa

            choices.append(choice)

            if selected:
                widget = DeletableLabel(
                            category=QueryForm.APPLIED_FILTERS_CATEGORY,
                            identifier=engine_value.identifier,
                            text=engine_value.label,
                            alternative_url=alternative_url)

                widgets.append(widget)

        if len(choices) <= 1:
            return []

        widget = Picker(category=QueryForm.FILTERS_CATEGORY,
                        identifier=identifier, label=parameter.label, choices=choices,
                        form_id=form.identifier)

        widgets.append(widget)

        return widgets
