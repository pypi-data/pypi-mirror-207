from django import template
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.templatetags.static import static

from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(takes_context=True, name="include_query_form_panel")
def include_query_form_panel_tag(context, panel):
    return panel.render(context=context.flatten())


@register.simple_tag(takes_context=True, name="query_result_range")
def query_result_range_tag(context, result_slice, *, form, wrapper_element='div',
                           result_label=None, result_label_plural=None, no_results_label=None,
                           classname='query-result-range'):

    if not result_slice:
        return ''

    result = result_slice.result

    if result_label is None:
        result_label = 'Result'

    if result_label_plural is None:
        result_label_plural = result_label + 's'

    if no_results_label is None:
        no_results_label = 'No ' + result_label_plural

    template_context = {
        'form': form,
        'result': result,
        'result_slice': result_slice,
        'result_label': result_label,
        'result_label_plural': result_label_plural,
        'no_results_label': no_results_label,
        'wrapper_element': wrapper_element,
        'classname': classname
    }

    return render_to_string(APP_LABEL + "/tags/query_result_range.html", context=template_context)


@register.simple_tag(takes_context=True, name="query_result_navigation")
def query_result_navigation_tag(context, result_slice, *, form, wrapper_element='div',
                                classname='query-result-navigation',
                                page_label=None, page_label_plural=None, no_pages_label=None,
                                include_previous=True, include_next=True, k=3):

    if not result_slice:
        return ''

    if page_label is None:
        page_label = 'Page'

    if page_label_plural is None:
        page_label_plural = page_label + 's'

    if no_pages_label is None:
        no_pages_label = 'No ' + page_label_plural

    result = result_slice.result

    slice_numbers = []

    for number in range(max(1, result_slice.number - k), result_slice.number):
        slice_numbers.append(number)

    slice_numbers.append(result_slice.number)

    for number in range(result_slice.number + 1, 1 + min(result.total_slice_count, result_slice.number + k)):
        slice_numbers.append(number)

    if slice_numbers[0] != 1:
        slice_numbers.insert(0, 1)

    if slice_numbers[-1] != result.total_slice_count:
        slice_numbers.append(result.total_slice_count)

    previous_link_and_label = None
    next_link_and_label = None

    previous_slice_number = result_slice.number - 1 if result_slice.number > 1 else None
    next_slice_number = result_slice.number + 1 if result_slice.number < result.total_slice_count else None

    if include_previous and previous_slice_number:
        slice_numbers.append(previous_slice_number)

    if include_next and next_slice_number:
        slice_numbers.append(next_slice_number)

    slice_urls = result.query.handler.build_slice_number_urls_for_result(form, result, slice_numbers)
    slice_labels = ["{:d}".format(number) for number in slice_numbers]

    if include_next and next_slice_number:
        slice_numbers = slice_numbers[:-1]

        next_link_and_label = slice_urls[-1], slice_labels[-1]

        slice_urls = slice_urls[:-1]
        slice_labels = slice_labels[:-1]

    if include_previous and previous_slice_number:
        slice_numbers = slice_numbers[:-1]

        previous_link_and_label = slice_urls[-1], slice_labels[-1]

        slice_urls = slice_urls[:-1]
        slice_labels = slice_labels[:-1]

    slice_choices = list(zip(slice_numbers, slice_labels, slice_urls))

    template_context = {
        'form': form,
        'result': result,
        'result_slice': result_slice,
        'wrapper_element': wrapper_element,
        'classname': classname,
        'slice_choices': slice_choices,
        'page_label': page_label,
        'page_label_plural': page_label_plural,
        'no_pages_label': no_pages_label,
        'previous_link_and_label': previous_link_and_label,
        'next_link_and_label': next_link_and_label
    }

    return render_to_string(APP_LABEL + "/tags/query_result_navigation.html", context=template_context)


@register.simple_tag(takes_context=False)
def querykit_support(*, container_element):

    if container_element == 'head':
        return format_html('<link rel="stylesheet" type="text/css" href="{}">',
                           static(APP_LABEL + '/css/querykit.css'))

    """
    if container_element == 'body':
        return format_html('<script type="text/javascript" src="{}"></script>',
                           static(APP_LABEL + '/js/querykit.js'))
    """

    return ''

