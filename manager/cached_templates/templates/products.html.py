# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456173185.226647
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
        __M_writer('\n  <h3>Product Catalog:</h3>\n  <hr />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Product Name</th>\n      <th>Product Type</th>\n      <th>Price</th>\n      <th>Description</th>\n      <th>Image</th>\n      <th>Date Added</th>\n      <th>Status</th>\n      <th>Purchase Date</th>\n      <th>Creation Date</th>\n      <th>Creator</th>\n      <th>Quantity</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
        for product in products:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n        <td>')
            __M_writer(str( product.__class__.className ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( product.price ))
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
                __M_writer('            <p class="quantity">10</p>\n            |\n            <a href="/catalog/product.get_quantity/')
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
        __M_writer('  </table>\n  <br />\n  <a href="/manager/products.create/" class="btn btn-primary">Create A New Product</a>\n\n  <!-- Modal -->\n  <div class="modal fade" id="delete_product_modal" tabindex="-1" role="dialog" >\n   <div class="modal-dialog" role="document">\n     <div class="modal-content">\n       <div class="modal-header">\n         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n         <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n       </div><!-- modal-header -->\n       <div class="modal-body">\n         Delete this event?\n       </div><!-- modal-body -->\n       <div class="modal-footer">\n         <a id="confirm_delete_product_button" href="" class="btn btn-danger">Delete</a>\n         <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n       </div><!-- modal-footer -->\n     </div><!-- modal-content -->\n   </div><!-- modal-dialog -->\n </div><!-- modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "line_map": {"28": 0, "36": 1, "41": 96, "47": 3, "54": 3, "55": 22, "56": 23, "57": 24, "58": 24, "59": 25, "60": 25, "61": 26, "62": 26, "63": 27, "64": 27, "65": 28, "66": 28, "67": 29, "68": 29, "69": 31, "70": 32, "71": 32, "72": 32, "73": 33, "74": 34, "75": 36, "76": 38, "77": 39, "78": 39, "79": 39, "80": 40, "81": 41, "82": 43, "83": 45, "84": 46, "85": 46, "86": 46, "87": 47, "88": 48, "89": 50, "90": 52, "91": 53, "92": 53, "93": 53, "94": 54, "95": 55, "96": 57, "97": 59, "98": 60, "99": 62, "100": 62, "101": 62, "102": 62, "103": 63, "104": 64, "105": 66, "106": 68, "107": 68, "108": 70, "109": 70, "110": 74, "116": 110}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
