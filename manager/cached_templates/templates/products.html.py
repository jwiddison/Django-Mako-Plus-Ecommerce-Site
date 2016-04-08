# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460067044.252403
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_area', 'column_container_type']


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
        products = context.get('products', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def column_container_type():
            return render_column_container_type(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'column_container_type'):
            context['self'].column_container_type(**pageargs)
        

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
        products = context.get('products', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Product Catalog:</h3>\n  <hr />\n  <br />\n  <a href="/manager/products.create/" class="btn btn-primary">Create A New Product</a>\n  <br />\n  <br />\n  <table class="table table-striped">\n    <tr>\n      <th>Product Name</th>\n      <th>Product Type</th>\n      <th>Price</th>\n      <th>Description</th>\n      <th>Category</th>\n      <th>Image</th>\n      <th>Date Added</th>\n      <th>Status</th>\n      <th>Purchase Date</th>\n      <th>Creation Date</th>\n      <th>Creator</th>\n      <th>Quantity</th>\n      <th>Edit | Delete</th>\n    </tr>\n')
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
            __M_writer(str(product.category))
            __M_writer('</td>\n        <td><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/pics/')
            __M_writer(str(product.get_image_filename()))
            __M_writer('" alt="')
            __M_writer(str(product.name))
            __M_writer('" class="img-responsive img-circle"/></td>\n')
            __M_writer('        <td>')
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
        __M_writer('  </table>\n  <!-- Modal -->\n  <div class="modal fade" id="delete_product_modal" tabindex="-1" role="dialog" >\n   <div class="modal-dialog" role="document">\n     <div class="modal-content">\n       <div class="modal-header">\n         <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n         <h4 class="modal-title" id="myModalLabel">Please Confirm</h4>\n       </div><!-- modal-header -->\n       <div class="modal-body">\n         Delete this Product?\n       </div><!-- modal-body -->\n       <div class="modal-footer">\n         <a id="confirm_delete_product_button" href="" class="btn btn-danger">Delete</a>\n         <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n       </div><!-- modal-footer -->\n     </div><!-- modal-content -->\n   </div><!-- modal-dialog -->\n </div><!-- modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_column_container_type(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def column_container_type():
            return render_column_container_type(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('  <div class="container-fluid">\n  <hr/>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "line_map": {"132": 3, "138": 3, "139": 5, "145": 139, "28": 0, "39": 1, "44": 8, "49": 113, "55": 10, "63": 10, "64": 33, "65": 34, "66": 35, "67": 35, "68": 36, "69": 36, "70": 37, "71": 37, "72": 38, "73": 38, "74": 39, "75": 39, "76": 40, "77": 40, "78": 40, "79": 40, "80": 40, "81": 40, "82": 49, "83": 49, "84": 49, "85": 51, "86": 52, "87": 52, "88": 52, "89": 53, "90": 54, "91": 56, "92": 58, "93": 59, "94": 59, "95": 59, "96": 60, "97": 61, "98": 63, "99": 65, "100": 66, "101": 66, "102": 66, "103": 67, "104": 68, "105": 70, "106": 72, "107": 73, "108": 73, "109": 73, "110": 74, "111": 75, "112": 77, "113": 79, "114": 80, "115": 82, "116": 82, "117": 82, "118": 82, "119": 83, "120": 84, "121": 86, "122": 88, "123": 88, "124": 90, "125": 90, "126": 94}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
