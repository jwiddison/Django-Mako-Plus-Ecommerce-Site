# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453326272.289056
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/411:413/Colonial_Heritage_Foundation/homepage/templates/faq.html'
_template_uri = 'faq.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_area', 'content_right', 'content_left', 'content']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
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
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n  <h1>Frequently Asked Questions</h1>\n  <hr/>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id="big_right">\n    <h1 class="q_a">A:</h1>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id="big_left">\n    <h1 class="q_a">Q:</h1>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Question:</h3>\n  <p><b>What is the Colonial Heritage Foundation?</b></p>\n  <h3>Answer:</h3>\n  <p>The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America\'s historical writings, the presentation of lectures and seminars regarding America\'s founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.</p>\n  <hr/>\n  <h3>Question:</h3>\n  <p><b>Why "colonial heritage"?</b></p>\n  <h3>Answer:</h3>\n  <p>At the Colonial Heritage Foundation, we believe that the core virtues present at our Nation\'s founding that make the United States of America the great nation that it is have slowly began to erode over time.  The purpose of the foundation is to help American find their "colonial heritage" and learn about those virtues that used to define what it meant to be an American.</p>\n  <hr/>\n  <h3>Question:</h3>\n  <p><b>Why would I want to be involved with the Colonial Heritage Foundation?</b></p>\n  <h3>Answer:</h3>\n  <p>We believe that all American people, whether born here, or from abroad can benefit from an education in what it means to be an American.  We believe taht knowing and embracing our colonial heritage will benefit every person who endevours to learn about it.</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "faq.html", "line_map": {"96": 9, "66": 3, "102": 21, "72": 3, "41": 1, "108": 21, "78": 15, "114": 108, "51": 13, "84": 15, "46": 7, "56": 19, "90": 9, "28": 0}, "source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/411:413/Colonial_Heritage_Foundation/homepage/templates/faq.html"}
__M_END_METADATA
"""
