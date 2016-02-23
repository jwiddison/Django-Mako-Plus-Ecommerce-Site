# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456209937.817151
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>All events:</h3>\n  <hr />\n  <br />\n  <a href="/manager/events.create/" class="btn btn-primary">Create A New event</a>\n  <br />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Event Name</th>\n      <th>Description</th>\n      <th>Start Date</th>\n      <th>End Date</th>\n      <th>Venue</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for event in events:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(event.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(event.description))
            __M_writer('</td>\n        <td>')
            __M_writer(str(event.start_date))
            __M_writer('</td>\n        <td>')
            __M_writer(str(event.end_date))
            __M_writer('</td>\n        <td>')
            __M_writer(str(event.venue))
            __M_writer('</td>\n        <td>\n          <a href="/manager/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('/">Edit</a>\n           |\n          <a href="/manager/events.delete/')
            __M_writer(str( event.id ))
            __M_writer('/" class="delete_event_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n\n  <!-- Modal -->\n  <div class="modal fade" id="delete_event_modal" tabindex="-1" role="dialog" >\n   <div class="modal-dialog" role="document">\n     <div class="modal-content">\n       <div class="modal-header">\n         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n         <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n       </div><!-- modal-header -->\n       <div class="modal-body">\n         Delete this event?\n       </div><!-- modal-body -->\n       <div class="modal-footer">\n         <a id="confirm_delete_event_button" href="" class="btn btn-danger">Delete</a>\n         <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n       </div><!-- modal-footer -->\n     </div><!-- modal-content -->\n   </div><!-- modal-dialog -->\n </div><!-- modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/events.html", "uri": "events.html", "source_encoding": "utf-8", "line_map": {"64": 24, "65": 25, "66": 25, "67": 27, "68": 27, "69": 29, "70": 29, "71": 33, "77": 71, "28": 0, "36": 1, "41": 53, "47": 3, "54": 3, "55": 19, "56": 20, "57": 21, "58": 21, "59": 22, "60": 22, "61": 23, "62": 23, "63": 24}}
__M_END_METADATA
"""
