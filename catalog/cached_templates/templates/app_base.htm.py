# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460090653.043038
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['transbox_start', 'maintainence_message', 'alert', 'parallax_end', 'top_content_area', 'content_left', 'column_container_type', 'transbox_end', 'maintainence_container', 'parallax_start', 'content_right']


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
        categories = context.get('categories', UNDEFINED)
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def parallax_end():
            return render_parallax_end(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def parallax_start():
            return render_parallax_start(context._locals(__M_locals))
        def transbox_start():
            return render_transbox_start(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def transbox_end():
            return render_transbox_end(context._locals(__M_locals))
        def column_container_type():
            return render_column_container_type(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'column_container_type'):
            context['self'].column_container_type(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n\n')
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


def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
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


def render_parallax_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_end():
            return render_parallax_end(context)
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
        __M_writer('homepage/media/pics/CHFLogo.png" class="img-responsive center-block" id="main_logo"/>\n')
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
        __M_writer('\n  <div style="position: fixed; margin-top:-100px" id="fixed_left">\n    <a id="all_products_button" class="btn btn-primary" href="/catalog/index/">View All Products</a>\n    <br />\n    <br />\n    <h5>Search For a Product:</h5>\n    <form method="GET" action="/catalog/search/">\n      <input type="text" name="q" class="form-control" placeholder="Search"/>\n      <br />\n      <input type="submit" value="Search" class="btn btn-primary"/>\n    </form>\n    <br />\n    <h5>Filter By Category:</h5>\n    <a href="/catalog/index">View All</a>\n    <br />\n')
        for category in categories:
            __M_writer('      <a href="/catalog/index/')
            __M_writer(str(category.id))
            __M_writer('">')
            __M_writer(str(category.name))
            __M_writer('</a></li>\n      <br />\n')
        __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_column_container_type(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def column_container_type():
            return render_column_container_type(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('  <div class="container-fluid">\n')
        __M_writer('  <br/>\n')
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


def render_maintainence_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_container():
            return render_maintainence_container(context)
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


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n  <div style="position: fixed; margin-top:-100px" id="fixed_right">\n    <h5>Recently Viewed Products:</h5>\n    <hr />\n')
        for p in request.shopping_cart.get_viewed_items():
            __M_writer('      <a href="/catalog/detail/')
            __M_writer(str(p.id))
            __M_writer('">\n        <div class="recent">\n          <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/pics/')
            __M_writer(str( p.get_image_filename() ))
            __M_writer('" alt="')
            __M_writer(str(p.name))
            __M_writer('" class="img-responsive img-circle center-block prod_img"/>\n          <p>')
            __M_writer(str( p.name ))
            __M_writer('</p>\n          <div class="clearfix"></div>\n        </div><!-- recent -->\n      </a>\n')
        __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"256": 41, "257": 41, "130": 59, "259": 43, "260": 43, "261": 43, "262": 43, "263": 43, "264": 44, "265": 44, "266": 49, "141": 60, "272": 266, "152": 54, "28": 0, "58": 1, "163": 3, "170": 3, "171": 4, "172": 4, "178": 14, "185": 14, "186": 29, "187": 30, "188": 30, "189": 30, "190": 30, "191": 30, "192": 33, "68": 12, "198": 7, "73": 34, "258": 43, "204": 7, "205": 9, "78": 50, "83": 53, "212": 56, "206": 11, "88": 54, "93": 55, "223": 58, "98": 56, "103": 58, "234": 53, "108": 59, "113": 60, "245": 36, "119": 55, "63": 5, "253": 36, "254": 40, "255": 41}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm", "uri": "app_base.htm"}
__M_END_METADATA
"""
