# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1458056243.458126
=======
_modified_time = 1458154600.038062
>>>>>>> image_carousel
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
<<<<<<< HEAD
_exports = ['navbar_title', 'footer', 'content_right', 'maintainence_message', 'content_left', 'maintainence_container', 'top_content_area', 'base_header', 'account_menu', 'menu', 'content', 'icon', 'alert', 'title']
=======
_exports = ['maintainence_container', 'content_left', 'icon', 'navbar_title', 'maintainence_message', 'content', 'base_header', 'menu', 'content_right', 'alert', 'account_menu', 'top_content_area', 'title', 'footer']
>>>>>>> image_carousel


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
<<<<<<< HEAD
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def icon():
            return render_icon(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def base_header():
            return render_base_header(context._locals(__M_locals))
=======
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def icon():
            return render_icon(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        def base_header():
            return render_base_header(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
>>>>>>> image_carousel
        def account_menu():
            return render_account_menu(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
<<<<<<< HEAD
=======
        def footer():
            return render_footer(context._locals(__M_locals))
>>>>>>> image_carousel
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n  <meta charset="UTF-8">\n  <head>\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n    <link rel="icon" type="img/ico" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/flagicon.gif">\n    <!-- Bootstrap minified CSS, and custom global CSS -->\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css" />\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.css" />\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  </head>\n  <body>\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_container'):
            context['self'].maintainence_container(**pageargs)
        

        __M_writer('\n\n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'base_header'):
            context['self'].base_header(**pageargs)
        

        __M_writer('\n    </header>\n\n    <!-- Body Content -->\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n        </div><!-- col-md-12 -->\n      </div><!-- row -->\n      <div class="row">\n        <div class="col-md-2">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n        </div><!-- left -->\n        <div class="col-md-8">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div><!-- center -->\n        <div class="col-md-2">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n        </div><!-- right -->\n      </div><!-- row -->\n    </div><!-- container -->\n\n    <!-- Footer Content-->\n    <!-- <footer class="navbar navbar-fixed-bottom"> -->\n    <footer>\n      <div class="container">\n        <div class="row">\n          <div class="col-md-12">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n          </div><!-- col-md-12 -->\n        </div><!-- row -->\n      </div><!-- container -->\n    </footer>\n\n    <!-- Javascript -->\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/moment.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-datetimepicker.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_navbar_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_title():
            return render_navbar_title(context)
        __M_writer = context.writer()
        __M_writer('\n                <a class="navbar-brand" href="/homepage/index">Colonial Herigate Foundation</a>\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
=======
def render_maintainence_container(context,**pageargs):
>>>>>>> image_carousel
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_container():
            return render_maintainence_container(context)
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
        __M_writer('\n      <div class="jumbotron">\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12">\n              <div id="maintainence_message">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_message'):
            context['self'].maintainence_message(**pageargs)
        
<<<<<<< HEAD
        __M_writer('\n              <i class="fa fa-instagram fa-2x"></i>&nbsp;&nbsp;\n              <i class="fa fa-twitter fa-2x"></i>&nbsp;&nbsp;\n              <i class="fa fa-facebook fa-2x"></i>&nbsp;&nbsp;\n              <p>Copyright &copy; ')
        __M_writer(str( current_year ))
        __M_writer(' Colonial Heritage Foundation</p>\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n            Put Right Content Here!\n          ')
=======

        __M_writer('\n              </div><!-- maintainence_message -->\n            </div><!-- col-md-12 -->\n          </div><!-- row -->\n        </div><!-- container -->\n      </div><!-- jumbotron -->\n    ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
        __M_writer('\n                ')
=======
def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n            Put Left Content Here!\n          ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n            Put Left Content Here!\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_container():
            return render_maintainence_container(context)
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
        __M_writer('\n      <div class="jumbotron">\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12">\n              <div id="maintainence_message">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_message'):
            context['self'].maintainence_message(**pageargs)
        

        __M_writer('\n              </div><!-- maintainence_message -->\n            </div><!-- col-md-12 -->\n          </div><!-- row -->\n        </div><!-- container -->\n      </div><!-- jumbotron -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n            TOP AREA!\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_base_header(context,**pageargs):
=======
def render_maintainence_message(context,**pageargs):
>>>>>>> image_carousel
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_title():
            return render_navbar_title(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def base_header():
            return render_base_header(context)
        def account_menu():
            return render_account_menu(context)
        def menu():
            return render_menu(context)
        def icon():
            return render_icon(context)
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('        <div id="alert">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('\n        </div><!-- alert -->\n        <!-- - - - - Navbar - - - - - -->\n        <nav class="navbar navbar-inverse navbar-fixed-top transparent" role="navigation">\n          <div class="container-fluid">\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="/homepage/index">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'icon'):
            context['self'].icon(**pageargs)
        

        __M_writer('\n              </a>\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_title'):
            context['self'].navbar_title(**pageargs)
        

        __M_writer('\n            </div><!-- navbar-header -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul class="nav navbar-nav">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n              </ul>\n              <ul class="nav navbar-nav navbar-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account_menu'):
            context['self'].account_menu(**pageargs)
        

        __M_writer('\n              </ul>\n            </div><!-- collapse -->\n          </div><!-- container -->\n        </nav>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def account_menu():
            return render_account_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if request.user.is_authenticated():
            __M_writer('                    <!-- Dropdown, logout, etc -->\n                    <li class = "dropdown">\n                      <a href = "#" class = "dropdown-toggle" data-toggle = "dropdown">Hello ')
            __M_writer(str( request.user ))
            __M_writer('! <b class = "caret"></b></a>\n                      <ul class = "dropdown-menu">\n                        <li><a href="/account/index">Account Summary</a></li>\n                        <li><a href="/account/edit">Edit Account Info</a></li>\n                        <li><a href="/account/change_password">Change Password</a></li>\n                        <li><a href="/manager/index">Admin</a></li>\n                        <li role="presentation" class="divider"></li>\n                        <li><a href=\'/account/logout/\'>Logout</a></li>\n                      </ul>\n                    </li>\n')
        else:
            __M_writer('                    <button class="btn btn-danger" id="loginbutton">Login</button>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_base_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def icon():
            return render_icon(context)
        def navbar_title():
            return render_navbar_title(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def base_header():
            return render_base_header(context)
        def menu():
            return render_menu(context)
        def alert():
            return render_alert(context)
        def account_menu():
            return render_account_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('        <div id="alert">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('\n        </div><!-- alert -->\n        <!-- - - - - Navbar - - - - - -->\n        <nav class="navbar navbar-inverse navbar-fixed-top transparent" role="navigation">\n          <div class="container-fluid">\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="/homepage/index">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'icon'):
            context['self'].icon(**pageargs)
        

        __M_writer('\n              </a>\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_title'):
            context['self'].navbar_title(**pageargs)
        

        __M_writer('\n            </div><!-- navbar-header -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n              <ul class="nav navbar-nav">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n              </ul>\n              <ul class="nav navbar-nav navbar-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account_menu'):
            context['self'].account_menu(**pageargs)
        

        __M_writer('\n              </ul>\n            </div><!-- collapse -->\n          </div><!-- container -->\n        </nav>\n      ')
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
        __M_writer('"><a href="/homepage/index">Home</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'about' else ''))
        __M_writer('"><a href="/homepage/about">About</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'terms' else ''))
        __M_writer('"><a href="/homepage/terms">Terms</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'faq' else ''))
        __M_writer('"><a href="/homepage/faq">FAQ</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'contact' else ''))
        __M_writer('"><a href="/homepage/contact">Contact</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_app == 'catalog' else ''))
        __M_writer('"><a href="/catalog/index">Catalog</a></li>\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_content(context,**pageargs):
=======
def render_content_right(context,**pageargs):
>>>>>>> image_carousel
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n            Put Center Content Here!\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_icon(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def icon():
            return render_icon(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n                  <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/flagicon.gif"/>\n                ')
=======
def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        __M_writer('\n          ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
<<<<<<< HEAD
        def alert():
            return render_alert(context)
=======
        request = context.get('request', UNDEFINED)
        def account_menu():
            return render_account_menu(context)
>>>>>>> image_carousel
        __M_writer = context.writer()
        __M_writer('\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Colonial Heritage Foundation')
=======
def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n            TOP AREA!\n          ')
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


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('              ')

                 ## Python to get current year for footer
        import datetime
        current_year = datetime.date.today().year
                      
        
        __M_writer('\n              <p>Copyright &copy; ')
        __M_writer(str( current_year ))
        __M_writer(' Colonial Heritage Foundation</p>\n              <i class="fa fa-instagram fa-2x pull-right"></i>\n              <i class="fa fa-twitter fa-2x pull-right"></i>\n              <i class="fa fa-facebook fa-2x pull-right"></i>\n            ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"source_encoding": "utf-8", "line_map": {"260": 59, "265": 63, "270": 75, "17": 6, "19": 0, "281": 78, "288": 78, "289": 79, "290": 80, "291": 82, "292": 82, "293": 92, "294": 93, "295": 95, "301": 67, "308": 67, "309": 69, "310": 69, "311": 69, "312": 70, "57": 7, "314": 71, "315": 71, "316": 72, "317": 72, "318": 73, "319": 73, "320": 74, "321": 74, "66": 13, "67": 14, "68": 14, "69": 16, "70": 16, "71": 17, "72": 17, "73": 20, "74": 20, "55": 4, "76": 24, "333": 119, "56": 6, "339": 57, "86": 100, "313": 70, "346": 57, "91": 109, "348": 58, "96": 116, "354": 43, "101": 121, "360": 43, "106": 126, "231": 40, "366": 13, "61": 7, "112": 156, "113": 156, "114": 157, "275": 95, "116": 158, "117": 158, "118": 159, "119": 159, "120": 160, "121": 160, "122": 162, "123": 162, "124": 162, "130": 61, "136": 61, "142": 137, "148": 137, "149": 139, "150": 139, "111": 148, "156": 143, "157": 147, "158": 147, "164": 124, "170": 124, "327": 119, "176": 30, "115": 157, "182": 30, "372": 13, "347": 58, "188": 114, "194": 114, "75": 20, "200": 24, "208": 24, "213": 31, "219": 107, "378": 372, "225": 107, "81": 37, "249": 40, "250": 42, "255": 44}, "uri": "/homepage/templates/base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm"}
=======
{"uri": "/homepage/templates/base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "line_map": {"256": 95, "262": 67, "269": 67, "270": 69, "271": 69, "272": 69, "273": 70, "274": 70, "19": 0, "276": 71, "277": 72, "278": 72, "279": 73, "280": 73, "281": 74, "282": 74, "288": 124, "294": 124, "300": 43, "306": 43, "55": 4, "312": 78, "57": 7, "61": 7, "319": 78, "320": 79, "321": 80, "66": 13, "67": 14, "68": 14, "69": 16, "70": 16, "71": 17, "72": 17, "73": 20, "74": 20, "75": 20, "76": 24, "56": 6, "338": 107, "86": 100, "344": 13, "91": 109, "350": 13, "96": 116, "356": 137, "101": 121, "17": 6, "106": 126, "231": 42, "364": 139, "111": 148, "112": 156, "113": 156, "114": 157, "275": 71, "116": 158, "117": 158, "118": 159, "119": 159, "120": 160, "121": 160, "122": 162, "123": 162, "124": 162, "362": 137, "130": 24, "363": 139, "138": 24, "371": 144, "322": 82, "143": 31, "323": 82, "149": 114, "324": 92, "155": 114, "325": 93, "161": 57, "326": 95, "168": 57, "169": 58, "170": 58, "370": 143, "176": 61, "115": 157, "182": 61, "372": 144, "188": 30, "194": 30, "200": 119, "332": 107, "206": 119, "212": 40, "378": 372, "230": 40, "81": 37, "236": 44, "241": 59, "246": 63, "251": 75}, "source_encoding": "utf-8"}
>>>>>>> image_carousel
__M_END_METADATA
"""
