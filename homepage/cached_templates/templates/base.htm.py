# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456165735.911135
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'alert', 'navbar_title', 'footer', 'content_right', 'content', 'base_header', 'maintainence_container', 'icon', 'content_left', 'menu', 'account_menu', 'top_content_area', 'maintainence_message']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def alert():
            return render_alert(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def maintainence_container():
            return render_maintainence_container(context._locals(__M_locals))
        def base_header():
            return render_base_header(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def navbar_title():
            return render_navbar_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def icon():
            return render_icon(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def account_menu():
            return render_account_menu(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def top_content_area():
            return render_top_content_area(context._locals(__M_locals))
        def maintainence_message():
            return render_maintainence_message(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
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
        __M_writer('homepage/media/bootstrap-datetimepicker.min.css" />\n')
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
        

        __M_writer('\n        </div><!-- right -->\n      </div><!-- row -->\n    </div><!-- container -->\n\n    <!-- Footer Content-->\n    <footer>\n      <div class="container">\n        <div class="row">\n          <div class="col-md-12">\n            ')
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


def render_navbar_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_title():
            return render_navbar_title(context)
        __M_writer = context.writer()
        __M_writer('\n                <a class="navbar-brand" href="/homepage/index">ColonialHeritage.org</a>\n              ')
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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_base_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def alert():
            return render_alert(context)
        def navbar_title():
            return render_navbar_title(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def icon():
            return render_icon(context)
        def base_header():
            return render_base_header(context)
        def account_menu():
            return render_account_menu(context)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('        <div id="alert">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'alert'):
            context['self'].alert(**pageargs)
        

        __M_writer('\n        </div><!-- alert -->\n        <!-- - - - - Navbar - - - - - -->\n        <nav class="navbar navbar-inverse navbar-fixed-top transparent" role="navigation">\n          <div class="container">\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="/homepage/index">\n                ')
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


def render_icon(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def icon():
            return render_icon(context)
        __M_writer = context.writer()
        __M_writer('\n                  <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/flagicon.gif"/>\n                ')
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


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' else ''))
        __M_writer('"><a href="/homepage/index">Home</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'about' else ''))
        __M_writer('"><a href="/homepage/about">About</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'terms' else ''))
        __M_writer('"><a href="/homepage/terms">Terms</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'faq' else ''))
        __M_writer('"><a href="/homepage/faq">FAQ</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'contact' else ''))
        __M_writer('"><a href="/homepage/contact">Contact</a></li>\n                  <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'admin' else ''))
        __M_writer('"><a href="/manager/index">Admin</a></li>\n                ')
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
            __M_writer('! <b class = "caret"></b></a>\n                      <ul class = "dropdown-menu">\n                        <li><a href="/account/index">Account Summary</a></li>\n                        <li><a href="/account/edit">Edit Account Info</a></li>\n                        <li><a href="/account/change_password">Change Password</a></li>\n                        <li role="presentation" class="divider"></li>\n                        <li><a href=\'/account/logout/\'>Logout</a></li>\n                      </ul>\n                    </li>\n')
        else:
            __M_writer('                    <button class="btn btn-danger" id="loginbutton">Login</button>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


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


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "source_encoding": "utf-8", "line_map": {"256": 93, "342": 78, "262": 23, "270": 23, "17": 6, "19": 0, "281": 56, "288": 56, "289": 57, "290": 57, "347": 91, "296": 112, "302": 112, "308": 66, "55": 4, "56": 6, "57": 7, "315": 66, "316": 68, "317": 68, "318": 68, "319": 69, "320": 69, "321": 70, "66": 13, "67": 14, "324": 71, "325": 72, "326": 72, "327": 73, "72": 17, "73": 19, "74": 19, "75": 19, "76": 23, "334": 77, "81": 36, "341": 77, "86": 98, "343": 79, "344": 81, "345": 81, "346": 90, "91": 107, "348": 93, "96": 114, "354": 105, "101": 119, "360": 105, "106": 124, "366": 29, "61": 7, "112": 150, "113": 150, "114": 151, "275": 30, "116": 152, "117": 152, "118": 153, "119": 153, "120": 154, "121": 154, "122": 156, "123": 156, "124": 156, "130": 13, "136": 13, "322": 70, "142": 42, "323": 71, "148": 42, "68": 14, "154": 60, "111": 142, "69": 16, "160": 60, "70": 16, "166": 134, "71": 17, "172": 134, "173": 136, "174": 136, "328": 73, "115": 151, "180": 140, "181": 141, "182": 141, "372": 29, "188": 122, "194": 122, "200": 117, "206": 117, "212": 39, "378": 372, "230": 39, "231": 41, "236": 43, "241": 58, "246": 62, "251": 74}, "filename": "/Users/Jordan/Documents/BYU/0 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/base.htm"}
__M_END_METADATA
"""
