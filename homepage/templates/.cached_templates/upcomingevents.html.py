# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487094283.049142
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/upcomingevents.html'
_template_uri = 'upcomingevents.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_text', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_content_text():
            return render_top_content_text(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_text'):
            context['self'].top_content_text(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_text(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_text():
            return render_top_content_text(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="text-center">\n    <h2>Upcoming Colonial Heritage Foundation Events</h2>\n    <a><span class="glyphicon glyphicon-chevron-down big_icon"></span></a>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div id="link_down"></div>\n  <h3>Upcoming Events</h3>\n  <hr />\n  <br />\n  <p class="lead">Take a look at upcoming Colonial Heritage Foundation events.  Be sure to visit our <a href="/contact">contact</a> page if you have any questions.</p>\n')
        __M_writer('      <table class="table table striped">\n        <tr>\n          <th>Event Name</th>\n          <th>Description</th>\n          <th>Start Date</th>\n          <th>End Date</th>\n          <th>Location</th>\n        </tr>\n')
        for event in events:
            __M_writer('          <tr>\n            <td>')
            __M_writer(str(event.name))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.description))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.start_date))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.end_date))
            __M_writer('</td>\n            <td>')
            __M_writer(str(event.venue))
            __M_writer('</td>\n          </tr>\n')
        __M_writer('      </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"66": 10, "73": 10, "74": 18, "75": 26, "76": 27, "77": 28, "78": 28, "79": 29, "80": 29, "81": 30, "82": 30, "83": 31, "84": 31, "85": 32, "86": 32, "87": 35, "28": 0, "93": 87, "38": 1, "43": 8, "48": 41, "54": 3, "60": 3}, "source_encoding": "utf-8", "uri": "upcomingevents.html", "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/upcomingevents.html"}
__M_END_METADATA
"""
