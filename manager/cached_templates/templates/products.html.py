# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459794006.122272
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        images = context.get('images', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context)
        images = context.get('images', UNDEFINED)
        products = context.get('products', UNDEFINED)
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
            __M_writer('</td>\n        <td>\n')
            for image in images:
                if image.product == product:
                    __M_writer('            <img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/pics/')
                    __M_writer(str( image.filename ))
                    __M_writer('" alt="')
                    __M_writer(str(product.name))
                    __M_writer('" class="img-responsive"/>\n            ')
                    break 
                    
                    __M_writer('\n')
            __M_writer('        </td>\n        <td>')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/manager/templates/products.html", "uri": "products.html", "line_map": {"133": 127, "28": 0, "38": 1, "43": 105, "49": 3, "58": 3, "59": 26, "60": 27, "61": 28, "62": 28, "63": 29, "64": 29, "65": 30, "66": 30, "67": 31, "68": 31, "69": 32, "70": 32, "71": 34, "72": 35, "73": 36, "74": 36, "75": 36, "76": 36, "77": 36, "78": 36, "79": 36, "80": 37, "82": 37, "83": 40, "84": 41, "85": 41, "86": 43, "87": 44, "88": 44, "89": 44, "90": 45, "91": 46, "92": 48, "93": 50, "94": 51, "95": 51, "96": 51, "97": 52, "98": 53, "99": 55, "100": 57, "101": 58, "102": 58, "103": 58, "104": 59, "105": 60, "106": 62, "107": 64, "108": 65, "109": 65, "110": 65, "111": 66, "112": 67, "113": 69, "114": 71, "115": 72, "116": 74, "117": 74, "118": 74, "119": 74, "120": 75, "121": 76, "122": 78, "123": 80, "124": 80, "125": 82, "126": 82, "127": 86}}
__M_END_METADATA
"""
