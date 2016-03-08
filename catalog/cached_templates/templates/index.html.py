# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457419442.054825
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_right', 'content', 'content_left']


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
        products = context.get('products', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        categories = context.get('categories', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n  <h5>Recently Viewed</h5>\n  <hr />\n  <p>Probably have to store it in the session</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for product in products:
            __M_writer('    <p>')
            __M_writer(str( product.image ))
            __M_writer('</p>\n    <p>')
            __M_writer(str( product.name ))
            __M_writer('</p>\n    <p>')
            __M_writer(str( product.price ))
            __M_writer('</p>\n    <p>')
            __M_writer(str( product.category ))
            __M_writer('</p>\n    <p>')
            __M_writer(str( product.__class__.className ))
            __M_writer('</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        categories = context.get('categories', UNDEFINED)
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n  <a class="btn btn-primary">View All Products</a>\n  <br />\n  <h5>Search</h5>\n  <hr />\n  <p>Text Box will go here.</p>\n  <br />\n  <h5>Category</h5>\n  <hr />\n  <a href="">View All</a>\n  <br />\n')
        for category in categories:
            __M_writer('    <a href="">')
            __M_writer(str(category.name))
            __M_writer('</a></li>\n    <br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"68": 30, "74": 20, "28": 0, "81": 20, "82": 21, "83": 22, "84": 22, "85": 22, "86": 23, "87": 23, "88": 24, "89": 24, "90": 25, "91": 25, "92": 26, "93": 26, "110": 15, "99": 3, "41": 1, "106": 3, "107": 14, "108": 15, "109": 15, "46": 18, "51": 28, "116": 110, "56": 34, "62": 30}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/index.html", "source_encoding": "utf-8", "uri": "index.html"}
__M_END_METADATA
"""
