# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460094684.188589
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['transbox_start', 'menu', 'parallax_end', 'cart', 'maintainence_container', 'transbox_end', 'column_layout', 'maintainence_message', 'parallax_start', 'navbar_title', 'alert', 'top_content_area']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def transbox_start():
            return render_transbox_start(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def parallax_end():
            return render_parallax_end(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def cart():
            return render_cart(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        def transbox_end():
            return render_transbox_end(context._locals(__M_locals))
        def column_layout():
            return render_column_layout(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def parallax_start():
            return render_parallax_start(context._locals(__M_locals))
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_title'):
            context['self'].navbar_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n\n# Include to remove parallax window\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'parallax_start'):
            context['self'].parallax_start(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'parallax_end'):
            context['self'].parallax_end(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'transbox_start'):
            context['self'].transbox_start(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'transbox_end'):
            context['self'].transbox_end(**pageargs)
        

        __M_writer('\n# Leave these blocks blank\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_container'):
            context['self'].maintainence_container(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_message'):
            context['self'].maintainence_message(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'column_layout'):
            context['self'].column_layout(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'cart'):
            context['self'].cart(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_transbox_start(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def transbox_start():
            return render_transbox_start(context)
        __M_writer = context.writer()
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
        __M_writer(str( 'active' if request.dmp_router_page == 'users' else ''))
        __M_writer('"><a href="/manager/users">Users</a></li>\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'products' else ''))
        __M_writer('"><a href="/manager/products">Products</a></li>\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'categories' else ''))
        __M_writer('"><a href="/manager/categories">Categories</a></li>\n')
        __M_writer('  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'venues' else ''))
        __M_writer('"><a href="/manager/venues">Venues</a></li>\n  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'events' else ''))
        __M_writer('"><a href="/manager/events">Events</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parallax_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_end():
            return render_parallax_end(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_cart(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def cart():
            return render_cart(context)
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


def render_transbox_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def transbox_end():
            return render_transbox_end(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_column_layout(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def column_layout():
            return render_column_layout(context)
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


def render_parallax_start(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_start():
            return render_parallax_start(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_title():
            return render_navbar_title(context)
        __M_writer = context.writer()
        __M_writer('\n  <a class="navbar-brand" href="/manager/index">CHFSales - Admin</a>\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"261": 3, "136": 13, "268": 3, "269": 4, "270": 4, "143": 13, "144": 15, "145": 15, "146": 15, "147": 16, "148": 16, "149": 17, "150": 17, "151": 19, "152": 19, "153": 19, "154": 20, "155": 20, "28": 0, "161": 25, "172": 33, "183": 29, "59": 1, "64": 7, "194": 27, "69": 11, "74": 21, "205": 32, "79": 24, "227": 24, "84": 25, "216": 30, "89": 26, "94": 27, "99": 29, "104": 30, "109": 31, "238": 9, "114": 32, "244": 9, "119": 33, "276": 270, "250": 31, "125": 26}}
__M_END_METADATA
"""
