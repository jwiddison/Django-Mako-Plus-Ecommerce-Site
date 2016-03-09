# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457410710.429047
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html'
_template_uri = 'products.html'
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
        products = context.get('products', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Product Catalog:</h3>\n  <hr />\n  <br />\n  <a href="/manager/products.create/" class="btn btn-primary">Create A New Product</a>\n  <br />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Product Name</th>\n      <th>Product Type</th>\n      <th>Price</th>\n      <th>Description</th>\n      <th>Image</th>\n      <th>Date Added</th>\n      <th>Status</th>\n      <th>Purchase Date</th>\n      <th>Creation Date</th>\n      <th>Creator</th>\n      <th>Quantity</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for product in products:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.__class__.className))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.price))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.image))
            __M_writer('</td>\n        <td>')
            __M_writer(str(product.add_date))
            __M_writer('</td>\n        <td>\n')
            if product.__class__.className == "Rental Product":
                __M_writer('            ')
                __M_writer(str(product.status))
                __M_writer('\n')
            else:
                __M_writer('            -\n')
            __M_writer('        </td>\n        <td>\n')
            if product.__class__.className == "Rental Product":
                __M_writer('            ')
                __M_writer(str(product.purchase_date))
                __M_writer('\n')
            else:
                __M_writer('            -\n')
            __M_writer('        </td>\n        <td>\n')
            if product.__class__.className == "Individual Product":
                __M_writer('            ')
                __M_writer(str(product.create_date))
                __M_writer('\n')
            else:
                __M_writer('            -\n')
            __M_writer('        </td>\n        <td>\n')
            if product.__class__.className == "Individual Product":
                __M_writer('            ')
                __M_writer(str(product.creator))
                __M_writer('\n')
            else:
                __M_writer('            -\n')
            __M_writer('        </td>\n        <td>\n')
            if product.__class__.className == "Bulk Product":
                __M_writer('            <span class="quantity">10</span>\n            |\n            <a href="/manager/products.get_quantity/')
                __M_writer(str(product.id))
                __M_writer('" data-id="')
                __M_writer(str(product.id))
                __M_writer('" class="glyphicon glyphicon-refresh"></a>\n')
            else:
                __M_writer('            -\n')
            __M_writer('        </td>\n        <td>\n          <a href="/manager/products.edit/')
            __M_writer(str( product.id ))
            __M_writer('/">Edit</a>\n           |\n          <a href="/manager/products.delete/')
            __M_writer(str( product.id ))
            __M_writer('/" class="delete_product_button">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n  <!-- Modal -->\n  <div class="modal fade" id="delete_product_modal" tabindex="-1" role="dialog" >\n   <div class="modal-dialog" role="document">\n     <div class="modal-content">\n       <div class="modal-header">\n         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n         <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n       </div><!-- modal-header -->\n       <div class="modal-body">\n         Delete this event?\n       </div><!-- modal-body -->\n       <div class="modal-footer">\n         <a id="confirm_delete_product_button" href="" class="btn btn-danger">Delete</a>\n         <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n       </div><!-- modal-footer -->\n     </div><!-- modal-content -->\n   </div><!-- modal-dialog -->\n </div><!-- modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 96, "47": 3, "54": 3, "55": 25, "56": 26, "57": 27, "58": 27, "59": 28, "60": 28, "61": 29, "62": 29, "63": 30, "64": 30, "65": 31, "66": 31, "67": 32, "68": 32, "69": 34, "70": 35, "71": 35, "72": 35, "73": 36, "74": 37, "75": 39, "76": 41, "77": 42, "78": 42, "79": 42, "80": 43, "81": 44, "82": 46, "83": 48, "84": 49, "85": 49, "86": 49, "87": 50, "88": 51, "89": 53, "90": 55, "91": 56, "92": 56, "93": 56, "94": 57, "95": 58, "96": 60, "97": 62, "98": 63, "99": 65, "100": 65, "101": 65, "102": 65, "103": 66, "104": 67, "105": 69, "106": 71, "107": 71, "108": 73, "109": 73, "110": 77, "116": 110}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html", "uri": "products.html"}
__M_END_METADATA
"""
