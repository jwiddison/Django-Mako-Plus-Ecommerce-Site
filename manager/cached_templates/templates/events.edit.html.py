# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455740652.744061
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_area']


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
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        areas = context.get('areas', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Edit Event:</h3>\n  <hr />\n  <br />\n  <form method="POST">\n    <table>\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <br />\n    <input type="submit" class="btn btn-primary" value="Save Changes" />\n  </form>\n  <br />\n  <h3>Areas at this Event:</h3>\n  <hr />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Area Name</th>\n      <th>Description</th>\n      <th>Place Number</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for area in areas:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(area.description))
            __M_writer('</td>\n        <td>')
            __M_writer(str(area.place_number))
            __M_writer('</td>\n        <td>\n          <a href="">Edit</a>\n           |\n          <a href="" class="delete_area_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 28, "65": 29, "66": 29, "67": 37, "37": 1, "60": 26, "42": 38, "48": 3, "73": 67, "56": 3, "57": 9, "58": 9, "59": 25, "28": 0, "61": 27, "62": 27, "63": 28}, "uri": "events.edit.html", "source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/events.edit.html"}
__M_END_METADATA
"""
