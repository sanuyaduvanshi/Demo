
import requests
from django.http import JsonResponse
import json
from django.urls import reverse


from django.core.mail import EmailMessage
from django.conf import settings as conf_settings
from django.template.loader import render_to_string
from django.core.mail import send_mail 
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import uuid
import threading
import random
from urllib.parse import quote
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
   
  
    @staticmethod
    def contactemail(request,user):
        print(user)
        
        mail_from = conf_settings.EMAIL_HOST_USER
        mail_to = user
        
        context_data = {
        'mail_from':mail_from,
        'mail_to': mail_to,
        'user':user,
        
        }
        text_content = render_to_string('{0}/templates/contactemail.html'.format(conf_settings.BASE_DIR), context=context_data)
        email = EmailMultiAlternatives("Inquiry Email ", text_content, conf_settings.EMAIL_HOST_USER, [mail_to])
        print('------------------------------------------------------------email',email)
        email.attach_alternative(text_content, 'text/html')
        EmailThread(email).start()
