# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456202914.902256
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/events.edit.html'
_template_uri = 'events.edit.html'
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
        form = context.get('form', UNDEFINED)
        event_id = context.get('event_id', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        event_id = context.get('event_id', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Edit Event:</h3>\n  <hr />\n  <br />\n  <form method="POST">\n    <table>\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <br />\n    <input type="submit" class="btn btn-primary" value="Save Changes" />\n  </form>\n  <br />\n  <h3>Areas at this Event:</h3>\n  <hr />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Area Name</th>\n      <th>Description</th>\n      <th>Place Number</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for area in areas:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(area.description))
            __M_writer('</td>\n        <td>')
            __M_writer(str(area.place_number))
            __M_writer('</td>\n        <td>\n          <a href="/manager/areas.edit/')
            __M_writer(str( area.id ))
            __M_writer('" class="edit_area_button" data-areaID="')
            __M_writer(str( area.id ))
            __M_writer('">Edit</a>\n           |\n          <a href="/manager/areas.delete/')
            __M_writer(str( area.id ))
            __M_writer('/" class="delete_area_button">Delete</a>\n        </td>\n')
            __M_writer('      </tr>\n')
        __M_writer('  </table>\n  <a href="/manager/areas.create/" class="btn btn-primary" id="new_area_button" data-eventID="')
        __M_writer(str( event_id ))
        __M_writer('">Create New Area</a>\n\n  <!-- Delete Modal -->\n  <div class="modal fade" id="delete_area_modal" tabindex="-1" role="dialog" >\n   <div class="modal-dialog" role="document">\n     <div class="modal-content">\n       <div class="modal-header">\n         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n         <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n       </div><!-- modal-header -->\n       <div class="modal-body">\n         Delete this area?\n       </div><!-- modal-body -->\n       <div class="modal-footer">\n         <a id="confirm_delete_area_button" href="" class="btn btn-danger">Delete</a>\n         <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n       </div><!-- modal-footer -->\n     </div><!-- modal-content -->\n   </div><!-- modal-dialog -->\n </div><!-- modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.edit.html", "source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/events.edit.html", "line_map": {"64": 27, "65": 28, "66": 28, "67": 29, "68": 29, "69": 31, "70": 31, "71": 31, "72": 31, "73": 33, "74": 33, "75": 36, "76": 38, "77": 39, "78": 39, "84": 78, "28": 0, "38": 1, "43": 59, "49": 3, "58": 3, "59": 9, "60": 9, "61": 25, "62": 26, "63": 27}}
__M_END_METADATA
"""
