# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456209876.129586
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
        __M_writer('\n  <h3>All Current Users:</h3>\n  <hr />\n  <br />\n  <a href="/manager/users.create/" class="btn btn-primary">Create A New User</a>\n  <br />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Username</th>\n      <th>First Name</th>\n      <th>Last Name</th>\n      <th>Email</th>\n      <th>Address 1</th>\n      <th>Address 2</th>\n      <th>City</th>\n      <th>State</th>\n      <th>Zip Code</th>\n      <th>Phone Number</th>\n      <th>Birth Date</th>\n      <th>Groups</th>\n      <th>Edit | Change Password | Delete</th>\n    </tr>\n')
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
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.birth))
            __M_writer('</td>\n        <td>')
            __M_writer(str(user.groups.values_list('name', flat=True)))
            __M_writer('</td>\n        <td>\n          <a href="/manager/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/">Edit</a>\n           |\n          <a href="/manager/users.password/')
            __M_writer(str( user.id ))
            __M_writer('/">Change Password</a>\n          |\n          <a href="/manager/users.delete/')
            __M_writer(str( user.id ))
            __M_writer('/" class="delete_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n\n  <!-- Modal -->\n  <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog" >\n   <div class="modal-dialog" role="document">\n     <div class="modal-content">\n       <div class="modal-header">\n         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n         <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n       </div><!-- modal-header -->\n       <div class="modal-body">\n         Delete this user?\n       </div><!-- modal-body -->\n       <div class="modal-footer">\n         <a id="confirm_delete_button" href="" class="btn btn-danger">Delete</a>\n         <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n       </div><!-- modal-footer -->\n     </div><!-- modal-content -->\n   </div><!-- modal-dialog -->\n </div><!-- modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/users.html", "uri": "users.html", "source_encoding": "utf-8", "line_map": {"64": 31, "65": 32, "66": 32, "67": 33, "68": 33, "69": 34, "70": 34, "71": 35, "72": 35, "73": 36, "74": 36, "75": 37, "76": 37, "77": 38, "78": 38, "79": 39, "80": 39, "81": 41, "82": 41, "83": 43, "84": 43, "85": 45, "86": 45, "87": 49, "28": 0, "93": 87, "36": 1, "41": 69, "47": 3, "54": 3, "55": 26, "56": 27, "57": 28, "58": 28, "59": 29, "60": 29, "61": 30, "62": 30, "63": 31}}
__M_END_METADATA
"""
