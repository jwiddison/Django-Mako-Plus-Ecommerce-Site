from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):
  
  ## GET = form method
  ## get = access the value in the dictionary python creates with the key 'yourname' 
  print('>>>>>>>>>>> your name was: ', request.GET.get('yourname'))
  print('>>>>>>>>>>> your email was: ', request.GET.get('email'))
  print('>>>>>>>>>>> your phone was: ', request.GET.get('phone'))
  print('>>>>>>>>>>> your message was: ', request.GET.get('message'))
  
  ## parameters from the email back to the browser just in case we need them later.
  template_vars = {
    'yourname': request.GET.get('yourname'),
    'email': request.GET.get('email'),
    'phone': request.GET.get('phone'),
    'message': request.GET.get('message'),
  }
  return dmp_render_to_response(request, 'contact.html', template_vars)