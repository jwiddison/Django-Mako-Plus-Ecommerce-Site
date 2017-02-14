# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487094262.82457
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/account/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_area']


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
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Account Summary</h3>\n  <hr />\n  <p>Thank you for creating an account with us.  Here is a summary of your account info:</p>\n  <br />\n  <table>\n    <tr>\n      <th>Username:</th>\n      <td>')
        __M_writer(str(request.user.username))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>Name:</th>\n      <td>')
        __M_writer(str( request.user.first_name ))
        __M_writer(' ')
        __M_writer(str(request.user.last_name))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>Address Line 1:</th>\n      <td>')
        __M_writer(str(request.user.address1))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>Address Line 2:</th>\n      <td>')
        __M_writer(str(request.user.address2))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>City:</th>\n      <td>')
        __M_writer(str(request.user.city))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>State:</th>\n      <td>')
        __M_writer(str(request.user.state))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>Zip Code:</th>\n      <td>')
        __M_writer(str(request.user.zip_code))
        __M_writer('</td>\n    </tr>\n    <tr>\n      <th>Phone Number:</th>\n      <td>')
        __M_writer(str(request.user.phone_number))
        __M_writer('</td>\n    </tr>\n  </table>\n\n  <br />\n\n')
        __M_writer('  <hr />\n  <br />\n  <a href="/account/edit" class="btn btn-primary">Edit Account Info</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 23, "65": 27, "66": 27, "67": 31, "68": 31, "69": 35, "70": 35, "71": 39, "72": 39, "73": 55, "79": 73, "28": 0, "36": 1, "41": 58, "47": 3, "54": 3, "55": 11, "56": 11, "57": 15, "58": 15, "59": 15, "60": 15, "61": 19, "62": 19, "63": 23}, "source_encoding": "utf-8", "uri": "index.html", "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/account/templates/index.html"}
__M_END_METADATA
"""
