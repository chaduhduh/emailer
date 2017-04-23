# -*- coding: utf-8 -*-`
"""
  Emailer
"""


# imports
import endpoints
import json
from protorpc import (
    remote,
    messages
)
from datetime import(
    datetime
)
from utils import(
    StringMessage
)
import webapp2
from google.appengine.api import mail, app_identity


# declarations
email = "pick1number@gmail.com"
SEND_EMAIL_REQUEST = endpoints.ResourceContainer(
    message=messages.StringField(1),
)

# Emailer API

@endpoints.api(name='emailer', version='v1')
class Emailer(remote.Service):
    """Configures and Manages Emailer Service."""

    # send email
    @endpoints.method(request_message=SEND_EMAIL_REQUEST,
                      response_message=StringMessage,
                      path='send-email',
                      name='send_email',
                      http_method='POST')
    def send_email(self, request):
        message = request.message or "No Message in Email"
        app_id = app_identity.get_application_id()
        subject = message
        body = message
        mail.send_mail('noreply@{}.appspotmail.com'.format(app_id),
                       email,
                       subject,
                       body)
        return StringMessage(message="OK")

# start api server with our api objects

api = endpoints.api_server([Emailer])
