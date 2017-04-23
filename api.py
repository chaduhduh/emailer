# -*- coding: utf-8 -*-`
"""
  Emailer
"""


# imports

import endpoints
from google.appengine.api import (
    mail,
    app_identity
)
from protorpc import (
    remote,
    messages
)
from utils import (
    StringMessage
)


# declarations

SEND_EMAIL_REQUEST = endpoints.ResourceContainer(
    recipient=messages.StringField(1),
    subject=messages.StringField(2),
    message=messages.StringField(3)
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
        if not request.recipient:
          raise endpoints.BadRequestException('no recipient');
        if not request.message:
          raise endpoints.BadRequestException('no message');
        if not request.subject:
          raise endpoints.BadRequestException('no subject');
        app_id = app_identity.get_application_id()
        recipient = request.recipient
        subject = request.subject
        body = request.message
        mail.send_mail('noreply@{}.appspotmail.com'.format(app_id),
                       recipient,
                       subject,
                       body)
        return StringMessage(message="OK")


# start api server with our api objects

api = endpoints.api_server([Emailer])
