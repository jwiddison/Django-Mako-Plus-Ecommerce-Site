# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459064677.735999
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['transbox_start', 'transbox_end', 'alert', 'parallax_start', 'top_content_area', 'parallax_end', 'content_right', 'maintainence_message', 'content_left', 'maintainence_container']


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
        def transbox_end():
            return render_transbox_end(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def parallax_end():
            return render_parallax_end(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def alert():
            return render_alert(context._locals(__M_locals))
        def parallax_start():
            return render_parallax_start(context._locals(__M_locals))
        def transbox_start():
            return render_transbox_start(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        recent_products_list = context.get('recent_products_list', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
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


def render_transbox_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def transbox_end():
            return render_transbox_end(context)
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


def render_parallax_start(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_start():
            return render_parallax_start(context)
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


def render_parallax_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_end():
            return render_parallax_end(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        recent_products_list = context.get('recent_products_list', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h5>Recently Viewed Products:</h5>\n  <hr />\n')
        for product in recent_products_list:
            __M_writer('    <a href="/catalog/detail/')
            __M_writer(str(product.id))
            __M_writer('">\n      <div class="recent">\n        <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/pics/')
            __M_writer(str( product.get_image_filename() ))
            __M_writer('" alt="')
            __M_writer(str(product.name))
            __M_writer('" class="img-responsive center-block prod_img"/>\n        <p>')
            __M_writer(str(product.name))
            __M_writer('</p>\n        <div class="clearfix"></div>\n      </div><!-- recent -->\n    </a>\n')
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
        def content_left():
            return render_content_left(context)
        categories = context.get('categories', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <a id="all_products_button" class="btn btn-primary" href="/catalog/index/">View All Products</a>\n  <br />\n  <br />\n  <h5>Search For a Product:</h5>\n  <form method="GET" action="/catalog/search/">\n    <input type="text" name="q" class="form-control"/>\n    <br />\n    <input type="submit" value="Search" class="btn btn-primary"/>\n  </form>\n\n  <br />\n  <h5>Filter By Category:</h5>\n  <a href="/catalog/index">View All</a>\n  <br />\n')
        for category in categories:
            __M_writer('    <a href="/catalog/index/')
            __M_writer(str(category.id))
            __M_writer('">')
            __M_writer(str(category.name))
            __M_writer('</a></li>\n    <br />\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/app_base.htm", "source_encoding": "utf-8", "uri": "app_base.htm", "line_map": {"171": 51, "134": 6, "194": 39, "145": 50, "156": 8, "91": 50, "164": 9, "165": 9, "28": 0, "199": 41, "182": 35, "56": 1, "61": 4, "190": 35, "191": 38, "192": 39, "193": 39, "66": 5, "195": 41, "196": 41, "197": 41, "198": 41, "71": 6, "200": 41, "201": 42, "202": 42, "76": 12, "208": 5, "81": 33, "163": 8, "86": 47, "219": 14, "229": 30, "96": 51, "226": 14, "227": 29, "228": 30, "101": 52, "230": 30, "231": 30, "232": 30, "106": 53, "238": 4, "112": 52, "249": 238, "123": 53}}
__M_END_METADATA
"""
