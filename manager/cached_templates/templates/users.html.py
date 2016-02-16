# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455587712.268667
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>All Users:</h3>\n  <hr />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Username</th>\n      <th>First Name</th>\n      <th>Last Name</th>\n      <th>Email</th>\n      <th>Address 1</th>\n      <th>Address 2</th>\n      <th>City</th>\n      <th>State</th>\n      <th>Zip Code</th>\n      <th>Phone Number</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for user in users:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(user.username))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.email))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.address1))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.address2))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.city))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.state))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.zip_code))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.phone_number))
            __M_writer('</td>\n        <td>\n          <a href="/manager/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/">Edit</a>\n           |\n          <button id="delete_button" class="btn btn-sm btn-danger">Delete</button>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n  <br />\n  <a href="/manager/users.create/" class="btn btn-primary">Create A New User</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "users.html", "source_encoding": "utf-8", "line_map": {"64": 26, "65": 27, "66": 27, "67": 28, "68": 28, "69": 29, "70": 29, "71": 30, "72": 30, "73": 31, "74": 31, "75": 32, "76": 32, "77": 34, "78": 34, "79": 40, "85": 79, "28": 0, "36": 1, "41": 43, "47": 3, "54": 3, "55": 21, "56": 22, "57": 23, "58": 23, "59": 24, "60": 24, "61": 25, "62": 25, "63": 26}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/users.html"}
__M_END_METADATA
"""
