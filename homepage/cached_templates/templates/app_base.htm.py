# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459830233.311851
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['alert', 'column_container_type', 'maintainence_message', 'maintainence_container']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def alert():
            return render_alert(context._locals(__M_locals))
        def column_container_type():
            return render_column_container_type(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'column_container_type'):
            context['self'].column_container_type(**pageargs)
        

        __M_writer('\n\n# Leave these blocks blank\n')
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


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_column_container_type(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def column_container_type():
            return render_column_container_type(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="container-fluid"></div>\n')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"68": 18, "102": 16, "41": 1, "42": 10, "47": 13, "79": 11, "113": 102, "52": 16, "85": 11, "57": 17, "91": 17, "28": 0, "62": 18}, "uri": "app_base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/app_base.htm"}
__M_END_METADATA
"""
