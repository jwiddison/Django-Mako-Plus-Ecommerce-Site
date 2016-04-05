# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459879404.463057
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'center_content_class']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def center_content_class():
            return render_center_content_class(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content_class'):
            context['self'].center_content_class(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
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
            __M_writer('</b></p>\n        <br />\n        <p>$')
            __M_writer(str( product.price ))
            __M_writer('</p>\n        <br />\n        <p>')
            __M_writer(str( product.category ))
            __M_writer('</p>\n        <br />\n        <p>')
            __M_writer(str( product.__class__.className ))
            __M_writer('</p>\n      </div><!-- tile -->\n    </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content_class(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content_class():
            return render_center_content_class(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-md-8" align="center">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html", "source_encoding": "utf-8", "line_map": {"64": 4, "65": 5, "66": 5, "67": 5, "68": 7, "69": 7, "70": 7, "71": 7, "72": 7, "73": 7, "74": 9, "75": 9, "76": 11, "77": 11, "78": 13, "79": 13, "80": 15, "81": 15, "87": 21, "28": 0, "93": 21, "99": 93, "39": 1, "44": 19, "49": 23, "55": 3, "63": 3}}
__M_END_METADATA
"""
