# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455724221.471493
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/venues.html'
_template_uri = 'venues.html'
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
        venues = context.get('venues', UNDEFINED)
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
        venues = context.get('venues', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>All venues:</h3>\n  <hr />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Venue Name</th>\n      <th>Address</th>\n      <th>City</th>\n      <th>State</th>\n      <th>Zip Code</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for venue in venues:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(venue.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(venue.address))
            __M_writer('</td>\n        <td>')
            __M_writer(str(venue.city))
            __M_writer('</td>\n        <td>')
            __M_writer(str(venue.state))
            __M_writer('</td>\n        <td>')
            __M_writer(str(venue.zip_code))
            __M_writer('</td>\n        <td>\n          <a href="/manager/venues.edit/')
            __M_writer(str( venue.id ))
            __M_writer('/">Edit</a>\n           |\n          <a href="/manager/venues.delete/')
            __M_writer(str( venue.id ))
            __M_writer('/" id="delete_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n  <br />\n  <a href="/manager/venues.create/" class="btn btn-primary">Create A New venue</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/venues.html", "source_encoding": "utf-8", "uri": "venues.html", "line_map": {"64": 21, "65": 22, "66": 22, "67": 24, "68": 24, "69": 26, "70": 26, "71": 30, "77": 71, "28": 0, "36": 1, "41": 33, "47": 3, "54": 3, "55": 16, "56": 17, "57": 18, "58": 18, "59": 19, "60": 19, "61": 20, "62": 20, "63": 21}}
__M_END_METADATA
"""