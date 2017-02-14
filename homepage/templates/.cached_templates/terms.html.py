# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487094291.433348
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/terms.html'
_template_uri = 'terms.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['top_content_area', 'content_left', 'content', 'content_right']


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
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content_area'):
            context['self'].top_content_area(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content_area(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content_area():
            return render_top_content_area(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/CHFLogo.png" class="img-responsive center-block" id="main_logo"/>\n  <hr/>\n  <br/>\n  <div class="text-center">\n    <h2>Terms of Use</h2>\n    <a><span class="glyphicon glyphicon-chevron-down big_icon"></span></a>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <!-- Terms of Use (pulled from Amazon.com) -->\n  <div id="link_down"></div>\n  <h3>Last updated: January 22, 2016</h3>\n  <p>Welcome to chfsales.com.  Colonial Heritage Foundation Services LLC and/or its affiliates ("Colonial Heritage Foundation") provide website features and other products and services to you when you visit or shop at Colonial Heritage Foundation.com, use Colonial Heritage Foundation products or services, use Colonial Heritage Foundation applications for mobile, or use software provided by Colonial Heritage Foundation in connection with any of the foregoing (collectively, "Colonial Heritage Foundation Services"). Colonial Heritage Foundation provides the Colonial Heritage Foundation Services subject to the following conditions.</p>\n  <p>By using Colonial Heritage Foundation Services, you agree to these conditions. Please read them carefully.</p>\n  <p>We offer a wide range of Services, and sometimes additional terms may apply. When you use an Colonial Heritage Foundation Service (for example, Your Profile, Gift Cards, Colonial Heritage Foundation Instant Video, Your Media Library, or Colonial Heritage Foundation applications for mobile) you also will be subject to the guidelines, terms and agreements applicable to that Colonial Heritage Foundation Service ("Service Terms"). If these Conditions of Use are inconsistent with the Service Terms, those Service Terms will control.</p>\n  <h3>PRIVACY</h3>\n  <p>Please review our Privacy Notice, which also governs your use of Colonial Heritage Foundation Services, to understand our practices.</p>\n  <h3>ELECTRONIC COMMUNICATIONS</h3>\n  <p>When you use any Colonial Heritage Foundation Service, or send e-mails, text messages, and other communications from your desktop or mobile device to us, you are communicating with us electronically. You consent to receive communications from us electronically. We will communicate with you in a variety of ways, such as by e-mail, text, in-app push notices, or by posting notices and messages on this site or through the other Colonial Heritage Foundation Services, such as our Message Center. You agree that all agreements, notices, disclosures, and other communications that we provide to you electronically satisfy any legal requirement that such communications be in writing.</p>\n  <h3>COPYRIGHT</h3>\n  <p>All content included in or made available through any Colonial Heritage Foundation Service, such as text, graphics, logos, button icons, images, audio clips, digital downloads, data compilations, and software is the property of Colonial Heritage Foundation or its content suppliers and protected by United States and international copyright laws. The compilation of all content included in or made available through any Colonial Heritage Foundation Service is the exclusive property of Colonial Heritage Foundation and protected by U.S. and international copyright laws.</p>\n  <h3>TRADEMARKS</h3>\n  <p>Click here to see a non-exhaustive list of Colonial Heritage Foundation trademarks. In addition, graphics, logos, page headers, button icons, scripts, and service names included in or made available through any Colonial Heritage Foundation Service are trademarks or trade dress of Colonial Heritage Foundation in the U.S. and other countries. Colonial Heritage Foundation\'s trademarks and trade dress may not be used in connection with any product or service that is not Colonial Heritage Foundation\'s, in any manner that is likely to cause confusion among customers, or in any manner that disparages or discredits Colonial Heritage Foundation. All other trademarks not owned by Colonial Heritage Foundation that appear in any Colonial Heritage Foundation Service are the property of their respective owners, who may or may not be affiliated with, connected to, or sponsored by Colonial Heritage Foundation.</p>\n  <h3>PATENTS</h3>\n  <p>One or more patents owned by Colonial Heritage Foundation apply to the Colonial Heritage Foundation Services and to the features and services accessible via the Colonial Heritage Foundation Services. Portions of the Colonial Heritage Foundation Services operate under license of one or more patents. Click here to see a non-exhaustive list of applicable Colonial Heritage Foundation patents and applicable licensed patents.</p>\n  <h3>LICENSE AND ACCESS</h3>\n  <p>Subject to your compliance with these Conditions of Use and your payment of any applicable fees, Colonial Heritage Foundation or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable license to access and make personal and non-commercial use of the Colonial Heritage Foundation Services. This license does not include any resale or commercial use of any Colonial Heritage Foundation Service, or its contents; any collection and use of any product listings, descriptions, or prices; any derivative use of any Colonial Heritage Foundation Service or its contents; any downloading, copying, or other use of account information for the benefit of any third party; or any use of data mining, robots, or similar data gathering and extraction tools. All rights not expressly granted to you in these Conditions of Use or any Service Terms are reserved and retained by Colonial Heritage Foundation or its licensors, suppliers, publishers, rightsholders, or other content providers. No Colonial Heritage Foundation Service, nor any part of any Colonial Heritage Foundation Service, may be reproduced, duplicated, copied, sold, resold, visited, or otherwise exploited for any commercial purpose without express written consent of Colonial Heritage Foundation. You may not frame or utilize framing techniques to enclose any trademark, logo, or other proprietary information (including images, text, page layout, or form) of Colonial Heritage Foundation without express written consent. You may not use any meta tags or any other "hidden text" utilizing Colonial Heritage Foundation\'s name or trademarks without the express written consent of Colonial Heritage Foundation. You may not misuse the Colonial Heritage Foundation Services. You may use the Colonial Heritage Foundation Services only as permitted by law. The licenses granted by Colonial Heritage Foundation terminate if you do not comply with these Conditions of Use or any Service Terms.</p>\n  <h3>YOUR ACCOUNT</h3>\n  <p>If you use any Colonial Heritage Foundation Service, you are responsible for maintaining the confidentiality of your account and password and for restricting access to your computer, and you agree to accept responsibility for all activities that occur under your account or password. Colonial Heritage Foundation does sell products for children, but it sells them to adults, who can purchase with a credit card or other permitted payment method. If you are under 18, you may use the Colonial Heritage Foundation Services only with involvement of a parent or guardian. Alcohol listings on Colonial Heritage Foundation are intended for adults. You must be at least 21 years of age to purchase alcohol, or use any site functionality related to alcohol. Colonial Heritage Foundation reserves the right to refuse service, terminate accounts, remove or edit content, or cancel orders in its sole discretion.</p>\n  <h3>COPYRIGHT COMPLAINTS</h3>\n  <p>Colonial Heritage Foundation respects the intellectual property of others. If you believe that your work has been copied in a way that constitutes copyright infringement, please follow our Notice and Procedure for Making Claims of Copyright Infringement.</p>\n  <h3>RISK OF LOSS</h3>\n  <p>All items purchased from Colonial Heritage Foundation are made pursuant to a shipment contract. This means that the risk of loss and title for such items pass to you upon our delivery to the carrier.</p>\n  <h3>RETURNS, REFUNDS AND TITLE</h3>\n  <p>Colonial Heritage Foundation does not take title to returned items until the item arrives at our fulfillment center. At our discretion, a refund may be issued without requiring a return. In this situation, Colonial Heritage Foundation does not take title to the refunded item. For more information about our returns and refunds, please see our Returns Center</p>\n  <h3>PRODUCT DESCRIPTIONS</h3>\n  <p>Colonial Heritage Foundation attempts to be as accurate as possible. However, Colonial Heritage Foundation does not warrant that product descriptions or other content of any Colonial Heritage Foundation Service is accurate, complete, reliable, current, or error-free. If a product offered by Colonial Heritage Foundation itself is not as described, your sole remedy is to return it in unused condition.</p>\n  <h3>OTHER BUSINESSES</h3>\n  <p>Parties other than Colonial Heritage Foundation operate stores, provide services, or sell product lines through the Colonial Heritage Foundation Services. In addition, we provide links to the sites of affiliated companies and certain other businesses. We are not responsible for examining or evaluating, and we do not warrant the offerings of, any of these businesses or individuals or the content of their Web sites. Colonial Heritage Foundation does not assume any responsibility or liability for the actions, product, and content of all these and any other third parties. You should carefully review their privacy statements and other conditions of use.</p>\n  <h3>DISPUTES</h3>\n  <p>Any dispute or claim relating in any way to your use of any Colonial Heritage Foundation Service, or to any products or services sold or distributed by Colonial Heritage Foundation or through Colonial Heritage Foundation.com will be resolved by binding arbitration, rather than in court, except that you may assert claims in small claims court if your claims qualify. The Federal Arbitration Act and federal arbitration law apply to this agreement.</p>\n  <p>There is no judge or jury in arbitration, and court review of an arbitration award is limited. However, an arbitrator can award on an individual basis the same damages and relief as a court (including injunctive and declaratory relief or statutory damages), and must follow the terms of these Conditions of Use as a court would.</p>\n  <p>To begin an arbitration proceeding, you must send a letter requesting arbitration and describing your claim to our registered agent Corporation Service Company, 300 Deschutes Way SW, Suite 304, Tumwater, WA 98501. The arbitration will be conducted by the American Arbitration Association (AAA) under its rules, including the AAA\'s Supplementary Procedures for Consumer-Related Disputes. The AAA\'s rules are available at www.adr.org or by calling 1-800-778-7879. Payment of all filing, administration and arbitrator fees will be governed by the AAA\'s rules. We will reimburse those fees for claims totaling less than $10,000 unless the arbitrator determines the claims are frivolous. Likewise, Colonial Heritage Foundation will not seek attorneys\' fees and costs in arbitration unless the arbitrator determines the claims are frivolous. You may choose to have the arbitration conducted by telephone, based on written submissions, or in person in the county where you live or at another mutually agreed location.</p>\n  <p>We each agree that any dispute resolution proceedings will be conducted only on an individual basis and not in a class, consolidated or representative action. If for any reason a claim proceeds in court rather than in arbitration we each waive any right to a jury trial. We also both agree that you or we may bring suit in court to enjoin infringement or other misuse of intellectual property rights.</p>\n  <h3>APPLICABLE LAW</h3>\n  <p>By using any Colonial Heritage Foundation Service, you agree that the Federal Arbitration Act, applicable federal law, and the laws of the state of Washington, without regard to principles of conflict of laws, will govern these Conditions of Use and any dispute of any sort that might arise between you and Colonial Heritage Foundation.</p>\n  <h3>SITE POLICIES, MODIFICATION, AND SEVERABILITY</h3>\n  <p>Please review our other policies, such as our pricing policy, posted on this site. These policies also govern your use of Colonial Heritage Foundation Services. We reserve the right to make changes to our site, policies, Service Terms, and these Conditions of Use at any time. If any of these conditions shall be deemed invalid, void, or for any reason unenforceable, that condition shall be deemed severable and shall not affect the validity and enforceability of any remaining condition.</p>\n  <h3>Additional Colonial Heritage Foundation Software Terms</h3>\n  <p>Use of the Colonial Heritage Foundation Software. You may use Colonial Heritage Foundation Software solely for purposes of enabling you to use and enjoy the Colonial Heritage Foundation Services as provided by Colonial Heritage Foundation, and as permitted by the Conditions of Use, these Software Terms and any Service Terms. You may not incorporate any portion of the Colonial Heritage Foundation Software into your own programs or compile any portion of it in combination with your own programs, transfer it for use with another service, or sell, rent, lease, lend, loan, distribute or sub-license the Colonial Heritage Foundation Software or otherwise assign any rights to the Colonial Heritage Foundation Software in whole or in part. You may not use the Colonial Heritage Foundation Software for any illegal purpose. We may cease providing any Colonial Heritage Foundation Software and we may terminate your right to use any Colonial Heritage Foundation Software at any time. Your rights to use the Colonial Heritage Foundation Software will automatically terminate without notice from us if you fail to comply with any of these Software Terms, the Conditions of Use or any other Service Terms. Additional third party terms contained within or distributed with certain Colonial Heritage Foundation Software that are specifically identified in related documentation may apply to that Colonial Heritage Foundation Software (or software incorporated with the Colonial Heritage Foundation Software) and will govern the use of such software in the event of a conflict with these Conditions of Use. All software used in any Colonial Heritage Foundation Service is the property of Colonial Heritage Foundation or its software suppliers and protected by United States and international copyright laws.</p>\n  <p><b>Use of Third Party Services:</b> When you use the Colonial Heritage Foundation Software, you may also be using the services of one or more third parties, such as a wireless carrier or a mobile platform provider. Your use of these third party services may be subject to the separate policies, terms of use, and fees of these third parties.</p>\n  <p><b>No Reverse Engineering:</b> You may not, and you will not encourage, assist or authorize any other person to copy, modify, reverse engineer, decompile or disassemble, or otherwise tamper with, the Colonial Heritage Foundation Software, whether in whole or in part, or create any derivative works from or of the Colonial Heritage Foundation Software.</p>\n  <p><b>Updates:</b> In order to keep the Colonial Heritage Foundation Software up-to-date, we may offer automatic or manual updates at any time and without notice to you.</p>\n  <p>Export Regulations; Government End Users. You must comply with all export and re-export restrictions and regulations of the Department of Commerce and other United States agencies and authorities that may apply to the Colonial Heritage Foundation Software. If you are a U.S. Government end user, we are licensing the Colonial Heritage Foundation Software to you as a "Commercial Item" as that term is defined in the U.S. Code of Federal Regulations (see 48 C.F.R. § 2.101), and the rights we grant you to the Colonial Heritage Foundation Software are the same as the rights we grant to all others under these Conditions of Use.</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"100": 13, "68": 3, "42": 1, "75": 3, "76": 4, "77": 4, "47": 11, "83": 62, "52": 59, "94": 13, "57": 62, "28": 0, "106": 63, "62": 63, "117": 106}, "source_encoding": "utf-8", "uri": "terms.html", "filename": "/Users/Jordan/Documents/BYU/4 - Senior Year/0 - Winter 2016/0 - 413/Colonial_Heritage_Foundation/homepage/templates/terms.html"}
__M_END_METADATA
"""
