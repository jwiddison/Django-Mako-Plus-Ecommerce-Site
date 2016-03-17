# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1458096931.922032
=======
_modified_time = 1458176319.462569
>>>>>>> image_carousel
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
<<<<<<< HEAD
_exports = ['title', 'content', 'content_right', 'icon', 'account_menu', 'base_header', 'alert', 'top_content_area', 'footer', 'navbar_title', 'menu', 'maintainence_message', 'content_left', 'maintainence_container']
=======
_exports = ['icon', 'content_right', 'base_header', 'alert', 'account_menu', 'menu', 'content_left', 'content', 'title', 'maintainence_message', 'maintainence_container', 'navbar_title', 'top_content_area', 'footer']
>>>>>>> image_carousel


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
<<<<<<< HEAD
        def title():
            return render_title(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def icon():
            return render_icon(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def account_menu():
            return render_account_menu(context._locals(__M_locals))
        def base_header():
            return render_base_header(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
=======
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def alert():
            return render_alert(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def icon():
            return render_icon(context._locals(__M_locals))
        def base_header():
            return render_base_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def account_menu():
            return render_account_menu(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n            Put Center Content Here!\n          ')
=======
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
>>>>>>> image_carousel
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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_icon(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def icon():
            return render_icon(context)
<<<<<<< HEAD
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n                  <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/flagicon.gif"/>\n                ')
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
        def account_menu():
            return render_account_menu(context)
        def base_header():
            return render_base_header(context)
        def alert():
            return render_alert(context)
=======
        def base_header():
            return render_base_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def alert():
            return render_alert(context)
        def account_menu():
            return render_account_menu(context)
>>>>>>> image_carousel
        def navbar_title():
            return render_navbar_title(context)
        def menu():
            return render_menu(context)
<<<<<<< HEAD
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def icon():
            return render_icon(context)
=======
>>>>>>> image_carousel
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
        

        __M_writer('\n              </ul>\n              <ul class="nav navbar-nav navbar-right">\n              <li><i class="fa fa-facebook fa-2x white"></i></li>\n              <li><i class="fa fa-instagram fa-2x white"></i></li>\n              <li><i class="fa fa-twitter fa-2x white"></i></li>\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account_menu'):
            context['self'].account_menu(**pageargs)
        

        __M_writer('\n              </ul>\n            </div><!-- collapse -->\n          </div><!-- container -->\n        </nav>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_alert(context,**pageargs):
<<<<<<< HEAD
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        __M_writer('\n          ')
=======
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        __M_writer = context.writer()
        __M_writer('\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def account_menu():
            return render_account_menu(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if request.user.is_authenticated():
            __M_writer('                    <!-- Dropdown, logout, etc -->\n                    <li class = "dropdown">\n                      <a href = "#" class = "dropdown-toggle" data-toggle = "dropdown">Hello ')
            __M_writer(str( request.user ))
            __M_writer('! <b class = "caret"></b></a>\n                      <ul class = "dropdown-menu">\n                        <li><a href="/account/index">Account Summary</a></li>\n                        <li><a href="/account/edit">Edit Account Info</a></li>\n                        <li><a href="/account/change_password">Change Password</a></li>\n                        <li><a href="/manager/index">Admin</a></li>\n                        <li role="presentation" class="divider"></li>\n                        <li><a href=\'/account/logout/\'>Logout</a></li>\n                      </ul>\n                    </li>\n')
        else:
            __M_writer('                    <button class="btn btn-danger" id="loginbutton">Login</button>\n')
        __M_writer('                ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context)
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
        __M_writer(' Colonial Heritage Foundation</p>\n            ')
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


def render_maintainence_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence_message():
            return render_maintainence_message(context)
        __M_writer = context.writer()
<<<<<<< HEAD
        __M_writer('\n                ')
=======
        __M_writer('\n      <div class="jumbotron">\n        <div class="container">\n          <div class="row">\n            <div class="col-md-12">\n              <div id="maintainence_message">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence_message'):
            context['self'].maintainence_message(**pageargs)
        

        __M_writer('\n              </div><!-- maintainence_message -->\n            </div><!-- col-md-12 -->\n          </div><!-- row -->\n        </div><!-- container -->\n      </div><!-- jumbotron -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_title():
            return render_navbar_title(context)
        __M_writer = context.writer()
        __M_writer('\n                <a class="navbar-brand" href="/homepage/index">Colonial Herigate Foundation</a>\n              ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n            Put Left Content Here!\n          ')
=======
def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        __M_writer = context.writer()
        __M_writer('\n            TOP AREA!\n          ')
>>>>>>> image_carousel
        return ''
    finally:
        context.caller_stack._pop_frame()


<<<<<<< HEAD
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
=======
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
{"source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "uri": "base.htm", "line_map": {"257": 43, "263": 110, "269": 110, "17": 6, "19": 0, "281": 140, "282": 142, "283": 142, "289": 146, "290": 147, "291": 147, "297": 61, "303": 61, "309": 67, "55": 4, "56": 6, "57": 7, "316": 67, "317": 69, "318": 69, "319": 69, "320": 70, "321": 70, "66": 13, "67": 14, "68": 14, "69": 16, "70": 16, "71": 17, "72": 17, "73": 20, "74": 20, "75": 20, "76": 24, "335": 30, "81": 37, "341": 30, "86": 103, "91": 112, "96": 119, "353": 117, "101": 124, "367": 24, "359": 24, "106": 129, "61": 7, "112": 156, "113": 156, "114": 157, "275": 140, "116": 158, "117": 158, "118": 159, "119": 159, "120": 160, "121": 160, "122": 162, "123": 162, "124": 162, "130": 13, "136": 13, "322": 71, "142": 122, "323": 71, "148": 122, "324": 72, "154": 127, "111": 148, "325": 72, "160": 127, "326": 73, "166": 57, "327": 73, "173": 57, "174": 58, "175": 58, "328": 74, "115": 157, "181": 81, "329": 74, "372": 31, "347": 117, "188": 81, "189": 82, "190": 83, "191": 85, "192": 85, "193": 95, "194": 96, "195": 98, "201": 40, "219": 40, "220": 42, "378": 372, "225": 44, "230": 59, "235": 63, "240": 75, "245": 98, "251": 43}}
=======
{"source_encoding": "utf-8", "uri": "base.htm", "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm", "line_map": {"256": 73, "257": 73, "258": 74, "259": 74, "265": 114, "271": 114, "17": 6, "19": 0, "277": 119, "283": 119, "289": 13, "295": 13, "301": 30, "307": 30, "55": 4, "56": 6, "57": 7, "61": 7, "321": 24, "66": 13, "67": 14, "68": 14, "69": 16, "70": 16, "71": 17, "72": 17, "73": 20, "74": 20, "75": 20, "76": 24, "81": 37, "338": 61, "86": 100, "313": 24, "344": 107, "91": 109, "350": 107, "96": 116, "356": 137, "101": 121, "106": 126, "363": 139, "364": 139, "111": 148, "112": 156, "113": 156, "114": 157, "115": 157, "116": 158, "117": 158, "118": 159, "119": 159, "120": 160, "121": 160, "122": 162, "123": 162, "124": 162, "362": 137, "130": 57, "137": 57, "138": 58, "139": 58, "145": 124, "151": 124, "157": 40, "326": 31, "370": 143, "175": 40, "176": 42, "371": 144, "181": 44, "372": 144, "186": 59, "191": 63, "196": 75, "201": 95, "207": 43, "213": 43, "332": 61, "219": 78, "378": 372, "226": 78, "227": 79, "228": 80, "229": 82, "230": 82, "231": 92, "232": 93, "233": 95, "239": 67, "246": 67, "247": 69, "248": 69, "249": 69, "250": 70, "251": 70, "252": 71, "253": 71, "254": 72, "255": 72}}
>>>>>>> image_carousel
__M_END_METADATA
"""
