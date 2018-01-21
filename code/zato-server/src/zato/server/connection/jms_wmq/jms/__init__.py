# -*- coding: utf-8 -*-

"""
Copyright (C) 2018, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# JMS constants

DELIVERY_MODE_NON_PERSISTENT = 1
DELIVERY_MODE_PERSISTENT = 2

RECEIVE_TIMEOUT_INDEFINITE_WAIT = 0
RECEIVE_TIMEOUT_NO_WAIT = -1

DEFAULT_DELIVERY_MODE = DELIVERY_MODE_PERSISTENT
DEFAULT_TIME_TO_LIVE = 0

class JMSException(Exception):
    """ Base class for all JMS-related exceptions.
    """

class NoMessageAvailableException(JMSException):
    """ Raised when the jms_template's call to receive returned no message
    in the expected wait interval.
    """

class WebSphereMQJMSException(JMSException):
    """ Class for exceptions related to WebSphereMQ only.
    """
    def __init__(self, message=None, completion_code=None, reason_code=None):
        JMSException.__init__(self, message)
        self.message = message
        self.completion_code = completion_code
        self.reason_code = reason_code
