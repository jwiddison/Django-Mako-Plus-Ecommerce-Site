# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457594024.163929
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_left', 'content_right', 'top_content_area', 'menu', 'alert', 'maintainence_container', 'maintainence_message']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        categories = context.get('categories', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
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


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        categories = context.get('categories', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <a class="btn btn-primary" href="/catalog/index/">View All Products</a>\n  <br />\n  <br />\n  <h5>Search For a Product:</h5>\n')
        __M_writer('  <form method="GET" action="/catalog/search/">\n    <input type="text" name="q" class="form-control"/>\n    <br />\n    <input type="submit" value="Search" class="btn btn-primary"/>\n  </form>\n\n  <br />\n  <h5>Filter By Category:</h5>\n  <a href="/catalog/index">View All</a>\n  <br />\n')
        for category in categories:
            __M_writer('    <a href="/catalog/index/')
            __M_writer(str(category.id))
            __M_writer('">')
            __M_writer(str(category.name))
            __M_writer('</a></li>\n    <br />\n')
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


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        def menu():
            return render_menu(context)
        request = context.get('request', UNDEFINED)
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


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
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


def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 6, "130": 8, "131": 9, "132": 9, "70": 12, "138": 42, "75": 34, "80": 40, "145": 42, "146": 44, "147": 44, "148": 44, "85": 47, "150": 45, "151": 46, "152": 46, "169": 4, "91": 14, "28": 0, "158": 6, "98": 14, "99": 20, "100": 30, "101": 31, "102": 31, "103": 31, "104": 31, "105": 31, "191": 180, "111": 36, "50": 1, "180": 5, "117": 36, "55": 4, "123": 8, "60": 5, "149": 45}, "uri": "app_base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
