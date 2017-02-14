# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478732967.10166
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'top_content_area', 'content_left', 'content_right']


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
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        sentmessage = context.get('sentmessage', UNDEFINED)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        sentmessage = context.get('sentmessage', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div id="link_down"></div>\n  <p class="lead text-center">Get in touch with someone from the colonial heritage foundation using the form below</p>\n\n  <div class="row">\n    <div class="col-md-3"></div>\n    <div class="col-md-6">\n      <div class="center-block text-center">\n      <p>')
        __M_writer(str(sentmessage))
        __M_writer('</p>\n        <form class="form-horizontal text-center" method="POST">\n          <table>\n            ')
        __M_writer(str(form.as_table()))
        __M_writer('\n          </table>\n          <input type="submit" class="btn btn-primary" value="Send" id="send_button">\n          <input type="reset" class="btn btn-default" value="Clear" id="clear_button">\n        </form>\n      </div>\n    </div>\n    <div class="col-md-3"></div>\n  </div>\n')
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
        __M_writer('\n  <div class="text-center">\n    <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/CHFLogo.png" class="img-responsive center-block" id="main_logo"/>\n    <hr/>\n    <br/>\n    <h2>Contact Us</h2>\n    <a><span class="glyphicon glyphicon-chevron-down big_icon"></span></a>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
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
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 36, "96": 5, "97": 5, "70": 13, "81": 24, "103": 35, "44": 1, "114": 36, "78": 13, "79": 21, "80": 21, "49": 11, "82": 24, "54": 33, "88": 3, "59": 35, "28": 0, "125": 114, "95": 3}, "uri": "contact.html", "source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/contact.html"}
__M_END_METADATA
"""
