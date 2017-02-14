# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487094303.124393
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/cart.html'
_template_uri = 'cart.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <h3>Shopping Cart</h3>\n')
        if request.shopping_cart.get_items() == []:
            __M_writer('  <p>Your cart is empty!  Please add some items.</p>\n')
        else:
            __M_writer('  <table class="table table-striped">\n    <tr>\n      <th>Item</th>\n      <th>Image</th>\n      <th>Price</th>\n      <th>Quantity</th>\n      <th>Extended</th>\n      <th>Action</th>\n    </tr>\n')
            for p in request.shopping_cart.get_items():
                __M_writer('    <tr>\n      <td><a href="/catalog/detail/')
                __M_writer(str(p.product_id))
                __M_writer('">')
                __M_writer(str(p.name))
                __M_writer('</a></td>\n      <td><img src="')
                __M_writer(str(STATIC_URL))
                __M_writer('catalog/media/pics/')
                __M_writer(str(p.filename))
                __M_writer('" class="img img-responsive img-circle cart_images" alt="')
                __M_writer(str(p.name))
                __M_writer('"</td>\n      <td>$')
                __M_writer(str(p.price))
                __M_writer('</td>\n      <td>')
                __M_writer(str(p.quantity))
                __M_writer('</td>\n      <td>$')
                __M_writer(str(p.calc_extended()))
                __M_writer('</td>\n      <td><a href="/catalog/cart.remove/')
                __M_writer(str(p.product_id))
                __M_writer('">Remove Item</a></td>\n    </tr>\n')
            __M_writer('    <tr> <!--Subtotal -->\n      <td><b>Subtotal:</b></td>\n      <td></td>\n      <td></td>\n      <td></td>\n      <td>$')
            __M_writer(str(request.shopping_cart.calc_subtotal()))
            __M_writer('</td>\n      <td></td>\n    </tr>\n    <tr> <!-- Tax -->\n      <td><b>Tax:</b></td>\n      <td></td>\n      <td></td>\n      <td></td>\n      <td>$')
            __M_writer(str(request.shopping_cart.calc_tax()))
            __M_writer('</td>\n      <td></td>\n    </tr>\n    <tr> <!-- Shipping -->\n      <td><b>Shipping:</b></td>\n      <td></td>\n      <td></td>\n      <td></td>\n      <td>$')
            __M_writer(str(request.shopping_cart.calc_shipping()))
            __M_writer('</td>\n      <td></td>\n    </tr>\n    <tr> <!-- Total Price -->\n      <td><b>Total:</b></td>\n      <td></td>\n      <td></td>\n      <td></td>\n      <td><b>$')
            __M_writer(str(request.shopping_cart.calc_total()))
            __M_writer('</b></td>\n      <td></td>\n    </tr>\n  </table>\n  <a href="/catalog/checkout" class="btn btn-primary">Checkout</a>\n  <a href="/catalog/cart.clear" class="btn btn-danger">Empty Cart</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 19, "65": 19, "66": 19, "67": 20, "68": 20, "69": 20, "70": 20, "71": 20, "72": 20, "73": 21, "74": 21, "75": 22, "76": 22, "77": 23, "78": 23, "79": 24, "80": 24, "81": 27, "82": 32, "83": 32, "84": 40, "85": 40, "86": 48, "87": 48, "88": 56, "89": 56, "28": 0, "95": 89, "37": 1, "42": 63, "48": 3, "56": 3, "57": 5, "58": 6, "59": 7, "60": 8, "61": 17, "62": 18, "63": 19}, "source_encoding": "utf-8", "uri": "cart.html", "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/catalog/templates/cart.html"}
__M_END_METADATA
"""
