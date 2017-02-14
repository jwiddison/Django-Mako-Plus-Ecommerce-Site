# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478732895.916788
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'column_container_type', 'cart', 'top_content_text', 'menu', 'transbox_end', 'column_layout', 'base_header', 'navbar_title', 'content_left', 'transbox_start', 'footer', 'content_right', 'alert', 'content', 'maintainence_container', 'maintainence_message', 'center_content_class', 'top_content_area', 'parallax_end', 'parallax_start', 'footer_outer']


from django_mako_plus import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def column_container_type():
            return render_column_container_type(context._locals(__M_locals))
        def top_content_text():
            return render_top_content_text(context._locals(__M_locals))
        def column_layout():
            return render_column_layout(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def parallax_start():
            return render_parallax_start(context._locals(__M_locals))
        def base_header():
            return render_base_header(context._locals(__M_locals))
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        def transbox_end():
            return render_transbox_end(context._locals(__M_locals))
        def cart():
            return render_cart(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def transbox_start():
            return render_transbox_start(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def alert():
            return render_alert(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def center_content_class():
            return render_center_content_class(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def parallax_end():
            return render_parallax_end(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def footer_outer():
            return render_footer_outer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n    <meta name="HandheldFriendly" content="True">\n    <meta name="MobileOptimized" content="320">\n    <meta name="viewport" content="initial-scale=1.0, minimum-scale=1.0, user-scalable=0">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n    <link rel="icon" type="img/ico" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/flagicon.gif">\n    <!-- Bootstrap minified CSS, and custom global CSS -->\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css" />\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.css" />\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/animate.css">\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  </head>\n  <body>\n\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_container'):
            context['self'].maintainence_container(**pageargs)
        

        __M_writer('\n\n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'base_header'):
            context['self'].base_header(**pageargs)
        

        __M_writer('\n    </header>\n\n    <!-- Body Content -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'parallax_start'):
            context['self'].parallax_start(**pageargs)
        

        __M_writer('\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'transbox_start'):
            context['self'].transbox_start(**pageargs)
        

        __M_writer('\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'transbox_end'):
            context['self'].transbox_end(**pageargs)
        

        __M_writer('\n            </div><!-- col-md-12 -->\n          </div><!-- row -->\n        </div><!-- container -->\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'parallax_end'):
            context['self'].parallax_end(**pageargs)
        

        __M_writer('\n\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'column_layout'):
            context['self'].column_layout(**pageargs)
        

        __M_writer('\n\n    <!-- Footer -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_outer'):
            context['self'].footer_outer(**pageargs)
        

        __M_writer('\n\n    <!-- Javascript -->\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/moment.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/parallax.min.js"></script>\n    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Colonial Heritage Foundation')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_column_container_type(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def column_container_type():
            return render_column_container_type(context)
        __M_writer = context.writer()
        __M_writer('\n        <div class="container">\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_cart(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def cart():
            return render_cart(context)
        __M_writer = context.writer()
        __M_writer('\n                  <a href="/catalog/cart/" class="btn btn-default" id="cartbutton">\n                    <span class="glyphicon glyphicon-shopping-cart"></span>\n                    <span class="cart_quantity">')
        __M_writer(str(request.shopping_cart.get_item_count()))
        __M_writer('</span>\n                  </a>\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_text(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_text():
            return render_top_content_text(context)
        __M_writer = context.writer()
        __M_writer('\n                    <div class="text-center">\n                      <h2>Welcome to CHFSales.com</h2>\n                      <a><span class="glyphicon glyphicon-chevron-down big_icon"></span></a>\n                    </div>\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' and request.dmp_router_app == 'homepage' else ''))
        __M_writer('"><a href="/">Home</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'about' else ''))
        __M_writer('"><a href="/about">About</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'terms' else ''))
        __M_writer('"><a href="/terms">Terms</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'faq' else ''))
        __M_writer('"><a href="/faq">FAQ</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'upcomingevents' else ''))
        __M_writer('"><a href="/upcomingevents">Upcoming Events</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'contact' else ''))
        __M_writer('"><a href="/contact">Contact</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_app == 'catalog' else ''))
        __M_writer('"><a href="/catalog">Shop</a></li>\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_transbox_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def transbox_end():
            return render_transbox_end(context)
        __M_writer = context.writer()
        __M_writer('\n                </div><!-- transbox -->\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_column_layout(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        def center_content_class():
            return render_center_content_class(context)
        def column_layout():
            return render_column_layout(context)
        def content_right():
            return render_content_right(context)
        def content():
            return render_content(context)
        def column_container_type():
            return render_column_container_type(context)
        __M_writer = context.writer()
        __M_writer('\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'column_container_type'):
            context['self'].column_container_type(**pageargs)
        

        __M_writer('\n        <div class="row">\n          <div class="col-md-2">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n          </div><!-- left -->\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content_class'):
            context['self'].center_content_class(**pageargs)
        

        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n          </div><!-- center -->\n          <div class="col-md-2">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n          </div><!-- right -->\n        </div><!-- row -->\n      </div><!-- container -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_base_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def alert():
            return render_alert(context)
        def menu():
            return render_menu(context)
        request = context.get('request', UNDEFINED)
        def base_header():
            return render_base_header(context)
        def navbar_title():
            return render_navbar_title(context)
        def cart():
            return render_cart(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('        <div id="alert">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('\n        </div><!-- alert -->\n        <!-- - - - - Navbar - - - - - -->\n        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n          <div class="container-fluid">\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="/">\n                <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/eagle.png" id="navbar_icon"/>\n              </a>\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_title'):
            context['self'].navbar_title(**pageargs)
        

        __M_writer('\n            </div><!-- navbar-header -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul class="nav navbar-nav">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n')
        __M_writer('                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'cart'):
            context['self'].cart(**pageargs)
        

        __M_writer('\n              </ul>\n              <ul class="nav navbar-nav navbar-right">\n                <li><a href="https://www.facebook.com/ColonialHeritageFoundation"><i class="fa fa-facebook-square fa-2x pull-right"></i></a></li>\n                <li><a href="https://www.instagram.com/colonial_heritage_foundation"><i class="fa fa-instagram fa-2x pull-right"></i></a></li>\n                <li><a href="http://www.colonialheritage.org/"><i class="fa fa-rss-square fa-2x pull-right"></i></a></li>\n')
        if request.user.is_authenticated():
            __M_writer('                  <li class = "dropdown">\n                    <a href = "#" class = "dropdown-toggle" data-toggle = "dropdown">Hello ')
            __M_writer(str( request.user ))
            __M_writer('! <b class = "caret"></b></a>\n                    <ul class = "dropdown-menu">\n                      <li><a href="/account/index">Account Summary</a></li>\n                      <li><a href="/account/edit">Edit Account Info</a></li>\n                      <li><a href="/account/change_password">Change Password</a></li>\n')
            if request.user.groups.all().filter(name='Manager') or request.user.groups.all().filter(name='SalesRep'):
                __M_writer('                        <li role="presentation" class="divider"></li>\n                        <li><a href="/manager/index">Admin</a></li>\n')
            __M_writer('                      <li role="presentation" class="divider"></li>\n                      <li><a href=\'/account/logout/\'>Logout</a></li>\n                    </ul>\n                  </li>\n')
        else:
            __M_writer('                  <button class="btn btn-danger" id="loginbutton">Login</button>\n')
        __M_writer('              </ul>\n            </div><!-- collapse -->\n          </div><!-- container -->\n        </nav>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_title():
            return render_navbar_title(context)
        __M_writer = context.writer()
        __M_writer('\n                <a class="navbar-brand" href="/">CHFSales</a>\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_transbox_start(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def transbox_start():
            return render_transbox_start(context)
        __M_writer = context.writer()
        __M_writer('\n              <div class="transbox">\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('                ')

        import datetime
        current_year = datetime.date.today().year
                        
        
        __M_writer('\n                <hr style="color:#E6272E"/>\n                <p id="footer_copy">Copyright &copy; ')
        __M_writer(str( current_year ))
        __M_writer(' Colonial Heritage Foundation</p>\n                <ul class="list-inline pull-right">\n                  <li>\n                    <a href="https://www.facebook.com/ColonialHeritageFoundation"><i class="fa fa-facebook-square fa-2x pull-right footer_buttons"></i></a>\n                  </li>\n                  <li>\n                    <a href="https://www.instagram.com/colonial_heritage_foundation"><i class="fa fa-instagram fa-2x pull-right footer_buttons"></i></a>\n                  </li>\n                  <li>\n                    <a href="http://www.colonialheritage.org/"><i class="fa fa-rss-square fa-2x pull-right footer_buttons"></i></a>\n                  </li>\n                </ul>\n                <hr style="color:#E6272E"/>\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        __M_writer('\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        def maintainence_container():
            return render_maintainence_container(context)
        __M_writer = context.writer()
        __M_writer('\n      <div class="jumbotron">\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12">\n              <div id="maintainence_message">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_message'):
            context['self'].maintainence_message(**pageargs)
        

        __M_writer('\n              </div><!-- maintainence_message -->\n            </div><!-- col-md-12 -->\n          </div><!-- row -->\n        </div><!-- container -->\n      </div><!-- jumbotron -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content_class(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content_class():
            return render_center_content_class(context)
        __M_writer = context.writer()
        __M_writer('\n          <div class="col-md-8">\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content_text():
            return render_top_content_text(context)
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n                  <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/CHFLogo.png" class="img-responsive center-block" id="top_image"/>\n                  <hr/>\n                  <br/>\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_text'):
            context['self'].top_content_text(**pageargs)
        

        __M_writer('\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parallax_end(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_end():
            return render_parallax_end(context)
        __M_writer = context.writer()
        __M_writer('\n        </div><!-- parallax-window -->\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parallax_start(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def parallax_start():
            return render_parallax_start(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n      <div class="parallax-window" data-parallax="scroll" data-image-src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/CHFcanon.JPG">\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_outer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        def footer_outer():
            return render_footer_outer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('      <footer>\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n            </div><!-- col-md-12 -->\n          </div><!-- row -->\n        </div><!-- container -->\n      </footer>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"342": 101, "266": 151, "343": 102, "271": 154, "17": 5, "530": 120, "19": 0, "276": 158, "558": 552, "345": 109, "281": 162, "538": 175, "346": 110, "286": 164, "517": 146, "546": 175, "291": 168, "552": 201, "297": 47, "402": 186, "477": 160, "313": 47, "314": 49, "319": 51, "320": 64, "321": 64, "395": 181, "326": 68, "71": 3, "72": 5, "73": 6, "331": 81, "332": 83, "77": 6, "397": 183, "505": 138, "337": 88, "82": 18, "83": 19, "84": 19, "85": 21, "86": 21, "87": 22, "88": 22, "89": 24, "90": 24, "91": 26, "92": 26, "93": 26, "94": 31, "471": 37, "344": 105, "353": 66, "99": 44, "523": 120, "359": 66, "104": 116, "454": 31, "404": 188, "109": 122, "532": 121, "114": 128, "371": 157, "446": 31, "119": 139, "377": 126, "396": 183, "124": 142, "403": 188, "383": 126, "129": 148, "389": 181, "134": 172, "139": 206, "140": 210, "141": 210, "142": 211, "143": 211, "144": 212, "145": 212, "146": 213, "147": 213, "148": 214, "149": 214, "150": 215, "151": 215, "152": 216, "153": 216, "410": 167, "159": 18, "416": 167, "165": 18, "422": 50, "171": 152, "428": 50, "483": 160, "177": 152, "434": 163, "499": 130, "183": 83, "440": 163, "500": 130, "347": 112, "190": 83, "191": 86, "192": 86, "198": 133, "459": 38, "204": 133, "465": 37, "210": 72, "547": 177, "531": 121, "365": 157, "217": 72, "218": 74, "219": 74, "220": 74, "221": 75, "222": 75, "223": 76, "224": 76, "225": 77, "226": 77, "227": 78, "228": 78, "229": 79, "230": 79, "231": 80, "232": 80, "489": 129, "338": 94, "238": 140, "498": 129, "339": 95, "244": 140, "340": 96, "250": 151, "511": 146, "341": 96}}
__M_END_METADATA
"""
