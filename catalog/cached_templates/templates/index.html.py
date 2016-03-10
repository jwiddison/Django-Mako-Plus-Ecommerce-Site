# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457585504.890545
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
        images = context.get('images', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        images = context.get('images', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        for product in products:
            __M_writer('    <div class="tile text-center">\n')
            for image in images:
                if image.product == product:
                    __M_writer('          <img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/pics/')
                    __M_writer(str( image.filename ))
                    __M_writer('" alt="')
                    __M_writer(str(product.name))
                    __M_writer('" class="img-responsive center-block prod_img"/>\n          ')
                    break 
                    
                    __M_writer('\n')
            __M_writer('      <br />\n      <p><b>')
            __M_writer(str( product.name ))
            __M_writer('</b></p>\n      <br />\n      <p>')
            __M_writer(str( product.price ))
            __M_writer('</p>\n      <br />\n      <p>')
            __M_writer(str( product.category ))
            __M_writer('</p>\n      <br />\n      <p>')
            __M_writer(str( product.__class__.className ))
            __M_writer('</p>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html", "source_encoding": "utf-8", "line_map": {"64": 8, "65": 8, "66": 8, "67": 8, "68": 8, "69": 8, "70": 9, "72": 9, "73": 12, "74": 13, "75": 13, "76": 15, "77": 15, "78": 17, "79": 17, "80": 19, "81": 19, "87": 81, "28": 0, "38": 1, "43": 22, "49": 3, "58": 3, "59": 4, "60": 5, "61": 6, "62": 7, "63": 8}}
__M_END_METADATA
"""
