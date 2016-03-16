# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458104290.947952
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_left', 'maintainence_message', 'maintainence_container', 'top_content_area', 'alert', 'content_right']


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
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        recent_products_list = context.get('recent_products_list', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        images = context.get('images', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
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
        

        __M_writer('\n')
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


def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
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
        images = context.get('images', UNDEFINED)
        recent_products_list = context.get('recent_products_list', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n  <h5>Recently Viewed Products:</h5>\n  <hr />\n')
        for product in recent_products_list:
            __M_writer('    <a href="/catalog/detail/')
            __M_writer(str(product.id))
            __M_writer('">\n      <div class="recent">\n')
            for image in images:
                if image.product == product:
                    __M_writer('            <img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/pics/')
                    __M_writer(str( image.filename ))
                    __M_writer('" alt="')
                    __M_writer(str(product.name))
                    __M_writer('" class="img-responsive center-block prod_img"/>\n            ')
                    break 
                    
                    __M_writer('\n')
            __M_writer('        <p>')
            __M_writer(str(product.name))
            __M_writer('</p>\n        <div class="clearfix"></div>\n      </div><!-- recent -->\n    </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm", "line_map": {"134": 8, "135": 9, "136": 9, "142": 6, "153": 36, "28": 0, "162": 36, "163": 39, "164": 40, "165": 40, "166": 40, "167": 42, "168": 43, "169": 44, "170": 44, "171": 44, "172": 44, "173": 44, "174": 44, "175": 44, "176": 45, "49": 1, "178": 45, "179": 48, "180": 48, "181": 48, "54": 4, "59": 5, "64": 6, "69": 12, "74": 34, "79": 53, "85": 14, "92": 14, "93": 20, "94": 30, "95": 31, "96": 31, "97": 31, "98": 31, "99": 31, "105": 5, "116": 4, "187": 181, "127": 8}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
