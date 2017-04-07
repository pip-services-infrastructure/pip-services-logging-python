# -*- coding: utf-8 -*-
"""
    pip_services_logging.data.version1.LogMessageV1
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Log message implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import datetime

from pip_services_commons.log import LogLevel
from pip_services_commons.errors import ErrorDescription

class LogMessageV1(object):
    time = None
    source = None
    level = None
    correlation_id = None
    error = None
    message = None

    def __init__(self, level = None, source = None, correlation_id = None, error = None, message = None):
        self.time = datetime.datetime.utcnow()
        self.level = level
        self.source = source
        self.correlation_id = correlation_id
        self.error = error
        self.message = message

    def to_json(self):
        return {
            'time': self.time,
            'source': self.source,
            'level': self.level,
            'correlation_id': self.correlation_id,
            'message': self.message,
            'error': self.error.to_json() if isinstance(self.error, ErrorDescription) else self.error
        }

    @staticmethod
    def from_json(json):
        if not isinstance(json, dict):
            return json
        
        log_message = LogMessageV1()
        log_message.time = json['time']
        log_message.source = json['source']
        log_message.level = json['level']
        log_message.correlation_id = json['correlation_id']
        log_message.message = json['message']
        log_message.error = ErrorDescription.from_json(json['error'])
        return log_message
