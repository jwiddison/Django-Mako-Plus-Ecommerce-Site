# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487094092.141336
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'top_content_text']


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
        def content():
            return render_content(context._locals(__M_locals))
        def top_content_text():
            return render_top_content_text(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_text'):
            context['self'].top_content_text(**pageargs)
        

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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id="link_down"></div>\n  <h3>Who Are We?</h3>\n  <p>The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America\'s historical writings, the presentation of lectures and seminars regarding America\'s founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.</p>\n  <h3>Education Exhibits</h3>\n  <p>At its heart, the Foundation is an educational institution.  One of its major undertakings is developing exhibits and programs that can help bring to life the history surrounding America\'s colonial period and is founding generation.  To this end, the Foundation has developed a variety of traveling exhibits.  One exhibit is focuses on the importance of the press in the American Revolution and of the continued importance of a free press in America today.  The central artifact of this exhibit is a replica of the Isaiah Thomas Press, an 18th century press that was influential building support for American independence.</p>\n  <p>Another exhibit focuses on the early colonial period and the ides of self-government that were planted in Jamestowne and Plimoth.  At the center of this exhibit is a scale model of the Mayflower. The exhibit also includes replicas of various artifacts from the early colonial period.</p>\n  <h3>Reading and Discussion Groups</h3>\n  <p>The Foundation coordinates and helps to establish community groups to encourage the reading and discussion of America\'s historical documents. For example, the Federalist Papers and the Anti-federalist Papers were publications that made the argument for and against the adoption of America\'s current constitution. The study and discussion of these documents can help Americans today understand the issues that were of most concern to our founding generation regarding the establishment of a strong federal government. These documents were written in a language style that is foreign to most contemporary readers. By providing recommended reading schedules, discussion questions, and materials to help modern readers read and grasp federal-period writings, the Foundation hopes to encourage small, community-based groups to undertake independent study of such founding documents. These discussion groups will be conducted year-round by volunteers and held in homes or community meeting places throughout the nation.</p>\n  <h3>Workshops, Lectures, and Seminars</h3>\n  <p>The Foundation sponsors lectures, seminars and workshops about the values, culture, skills, and history of America\'s founding era. Such events may be coordinated with universities and other educationally-focused organizations to educate adults about the sacrifices that early Americans made to provide today\'s population with the freedoms we enjoy. These events  seek to inspire individuals to engage in community-based educational activities to increase exposure an awareness of the history surrounding America\'s founding. Lectures, seminars and workshops are coordinated and presented year-round by Foundation volunteers. Depending on the venue, they are offered either free of charge or for a fee.</p>\n  <h3>Historical Reenactment</h3>\n  <p>The Foundation sponsors the Colonial Heritage Festival, the largest colonial living and reenactment event west of the Mississippi River. This event is located in Orem, Utah as is attended by more than 40,000 people annually.</p>\n  <p>The Foundation also coordinates presentations of individual reenactors portraying notable figures from the American founding such as  George Washington, Benjamin Franklin, and others.</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_text(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_text():
            return render_top_content_text(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="text-center">\n    <h2>Learn a Little More About Us</h2>\n    <a><span class="glyphicon glyphicon-chevron-down big_icon"></span></a>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "about.html", "line_map": {"65": 3, "59": 10, "53": 10, "71": 3, "42": 8, "47": 24, "28": 0, "77": 71, "37": 1}, "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/about.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
