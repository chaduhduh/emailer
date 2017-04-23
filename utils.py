"""collects general utility functions used by various areas of app"""


# imports

import logging
from google.appengine.ext import ndb
import endpoints
from protorpc import messages


# methods

class StringMessage(messages.Message):
    """StringMessage outbound (single) string message"""

    message = messages.StringField(1, required=True)
