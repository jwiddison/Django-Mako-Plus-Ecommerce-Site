# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457548209.928473
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['maintainence_container', 'top_content_area', 'menu', 'maintainence_message', 'content_left', 'alert', 'content_right']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        categories = context.get('categories', UNDEFINED)
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n# Leave these blocks blank\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_container'):
            context['self'].maintainence_container(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_message'):
            context['self'].maintainence_message(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_container():
            return render_maintainence_container(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n  <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/CHFLogo.png" class="img-responsive center-block" id="main_logo"/>\n  <hr/>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' else ''))
        __M_writer('"><a href="/catalog/index">Catalog</a></li>\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'search' else ''))
        __M_writer('"><a href="/catalog/search">Search</a></li>\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'detail' else ''))
        __M_writer('"><a href="/catalog/detail">Detail</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
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
        __M_writer('\n  <a class="btn btn-primary" href="/catalog/index/">View All Products</a>\n  <br />\n  <h5>Search</h5>\n')
        __M_writer('  <hr />\n  <p>Text Box will go here.</p>\n  <br />\n  <h5>Category</h5>\n  <hr />\n  <a href="">View All</a>\n  <br />\n')
        for category in categories:
            __M_writer('    <a href="/catalog/index/')
            __M_writer(str(category.id))
            __M_writer('">')
            __M_writer(str(category.name))
            __M_writer('</a></li>\n    <br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "app_base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm", "line_map": {"128": 41, "65": 6, "130": 42, "131": 42, "70": 12, "129": 41, "137": 5, "75": 30, "80": 36, "156": 19, "148": 14, "85": 43, "91": 4, "28": 0, "157": 26, "158": 27, "159": 27, "160": 27, "161": 27, "162": 27, "155": 14, "102": 8, "168": 6, "124": 38, "109": 8, "110": 9, "111": 9, "50": 1, "179": 32, "117": 38, "55": 4, "185": 32, "191": 185, "60": 5, "125": 40, "126": 40, "127": 40}}
__M_END_METADATA
"""
