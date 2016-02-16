# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455659643.103817
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html'
_template_uri = 'products.html'
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
        type = context.get('type', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        type = context.get('type', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>All Products:</h3>\n  <hr />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Product Name</th>\n      <th>Product Type</th>\n      <th>Description</th>\n      <th>Image</th>\n      <th>Date Added</th>\n      <th>Other Info</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for product in products:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str( type(product) ))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.image))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.add_date))
            __M_writer('</td>\n        <td>\n          Rental Product\n')
            __M_writer('        </td>\n        <td>\n          <a href="/manager/products.edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\n           |\n          <a href="/manager/products.delete/')
            __M_writer(str( product.id ))
            __M_writer('/" id="delete_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n  <br />\n  <a href="/manager/products.create/" class="btn btn-primary">Create A New Product</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 21, "65": 22, "66": 22, "67": 23, "68": 23, "69": 33, "70": 35, "71": 35, "72": 37, "73": 37, "74": 41, "80": 74, "28": 0, "37": 1, "42": 44, "48": 3, "56": 3, "57": 17, "58": 18, "59": 19, "60": 19, "61": 20, "62": 20, "63": 21}, "source_encoding": "utf-8", "uri": "products.html", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html"}
__M_END_METADATA
"""
