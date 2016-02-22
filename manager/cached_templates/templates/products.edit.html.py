# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456180775.315844
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.edit.html'
_template_uri = 'products.edit.html'
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
        form = context.get('form', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        product_type = context.get('product_type', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context)
        product_type = context.get('product_type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Edit product info:</h3>\n  <hr />\n  <br />\n  <form method="POST">\n    <table>\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <br />\n    <input id="pType_saved" type="submit" class="btn btn-primary" value="Save Changes" data-pType="')
        __M_writer(str(product_type))
        __M_writer('"/>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.edit.html", "source_encoding": "utf-8", "line_map": {"48": 3, "66": 60, "37": 1, "56": 3, "57": 9, "42": 14, "59": 12, "28": 0, "58": 9, "60": 12}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.edit.html"}
__M_END_METADATA
"""
