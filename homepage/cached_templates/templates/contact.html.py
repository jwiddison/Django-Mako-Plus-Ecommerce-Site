# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459404338.391097
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_area', 'content_left', 'content', 'content_right']


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
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
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


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="text-center">\n    <h1>Contact</h1>\n    <hr/>\n    <br/>\n    <p class="lead">Get in touch with someone from the colonial heritage foundation using the form below</p>\n    <a><span class="glyphicon glyphicon-chevron-down animated infinite swing big_icon"></span></a>\n  </div>\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="clearfix" id="link_to_form"></div>\n  <div class="row">\n    <div class="col-md-10">\n      <!--Email form-->\n      <form class="form-horizontal" method="get" action="/contact" enctype="multipart/form-data">\n        <div class="form-group">\n            <label class="control-label col-xs-3" for="name">Name:</label>\n            <div class="col-xs-9">\n                <input type="text" name="yourname" class="form-control" id="inputName" placeholder="Name">\n            </div><!-- col-xs-9 -->\n        </div><!-- form-group -->\n        <div class="form-group">\n            <label class="control-label col-xs-3" for="email">Email:</label>\n            <div class="col-xs-9">\n                <input type="text" name="email" class="form-control" id="inputEmail" placeholder="Email">\n            </div><!-- col-xs-9 -->\n        </div><!-- form-group -->\n        <div class="form-group">\n            <label class="control-label col-xs-3" for="phone">Phone:</label>\n            <div class="col-xs-9">\n                <input type="text" name="phone" class="form-control" id="inputPhone" placeholder="Phone">\n            </div><!-- col-xs-9 -->\n        </div><!-- form-group -->\n        <div class="form-group">\n            <label class="control-label col-xs-3" for="message">Message:</label>\n            <div class="col-xs-9">\n                <textarea rows="3" name="message" class="form-control" id="inputMessage" placeholder="Message"></textarea>\n            </div><!-- col-xs-9 -->\n        </div><!-- form-group -->\n        <div class="form-group">\n            <div class="col-xs-offset-3 col-xs-9">\n                <input type="submit" class="btn btn-primary" value="Send">\n                <input type="reset" class="btn btn-default" value="Clear">\n            </div><!-- col-xs-offset-3 col-xs-9 -->\n        </div><!-- form-group -->\n      </form>\n    </div><!-- col-md-10 -->\n    <div class="col-md-2"></div>\n  </div><!-- row -->\n')
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
{"uri": "contact.html", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/contact.html", "source_encoding": "utf-8", "line_map": {"96": 13, "67": 3, "102": 56, "73": 3, "46": 11, "79": 55, "113": 102, "51": 53, "41": 1, "56": 55, "90": 13, "28": 0, "61": 56}}
__M_END_METADATA
"""
