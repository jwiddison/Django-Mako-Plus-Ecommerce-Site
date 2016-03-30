# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459290218.088657
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for product in products:
            __M_writer('    <a href="/catalog/detail/')
            __M_writer(str(product.id))
            __M_writer('">\n      <div class="tile text-center center-block animated slideUpIn">\n        <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/pics/')
            __M_writer(str( product.get_image_filename() ))
            __M_writer('" alt="')
            __M_writer(str(product.name))
            __M_writer('" class="img-responsive center-block prod_img"/>\n        <br />\n        <p><b>')
            __M_writer(str( product.name ))
            __M_writer('</b></p>\n        <br />\n        <p>')
            __M_writer(str( product.price ))
            __M_writer('</p>\n        <br />\n        <p>')
            __M_writer(str( product.category ))
            __M_writer('</p>\n        <br />\n        <p>')
            __M_writer(str( product.__class__.className ))
            __M_writer('</p>\n      </div><!-- tile -->\n    </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 7, "65": 7, "66": 7, "67": 9, "68": 9, "69": 11, "70": 11, "71": 13, "72": 13, "73": 15, "74": 15, "80": 74, "28": 0, "37": 1, "42": 19, "48": 3, "56": 3, "57": 4, "58": 5, "59": 5, "60": 5, "61": 7, "62": 7, "63": 7}, "uri": "index.html", "source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html"}
__M_END_METADATA
"""
