# -*- coding: utf-8 -*-
"""
    tests.logic.test_LoggingController
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import datetime

from pip_services_commons.refer import References, Descriptor
from pip_services_commons.log import LogLevel
from pip_services_commons.data import FilterParams
from pip_services_commons.errors import ErrorDescriptionFactory
from pip_services_logging.persistence.LoggingMemoryPersistence import LoggingMemoryPersistence
from pip_services_logging.logic.LoggingController import LoggingController
from pip_services_logging.data.version1.LogMessageV1 import LogMessageV1

class TestLoggingController:
    controller = None

    @staticmethod
    def setup_class(cls):
        persistence = LoggingMemoryPersistence()
        cls.controller = LoggingController()
    
        references = References.from_tuples(
            Descriptor('pip-services-logging', 'persistence', 'memory', 'default', '1.0'), persistence,
            Descriptor('pip-services-logging', 'controller', 'default', 'default', '1.0'), cls.controller
        )
        cls.controller.set_references(references)

    def setup_method(self, method):
        self.controller.clear(None)

    def test_crud_operations(self):
        message = self.controller.write_message(
            None, 
            LogMessageV1(LogLevel.Info, None, "123", None, "AAA")
        )
        assert None != message

        message1 = LogMessageV1(LogLevel.Debug, None, "123", None, "BBB")
        message2 = LogMessageV1(LogLevel.Error, None, "123", ErrorDescriptionFactory.create(Exception('Test error')), "AAB")
        message2.time = datetime.datetime(1975, 1, 1, 0, 0, 0, 0)
        self.controller.write_messages(
            None,
            [message1, message2]
        )

        page = self.controller.read_messages(
            None, 
            FilterParams.from_tuples("search", "AA"), 
            None
        )
        assert 2 == len(page.data)

        page = self.controller.read_errors(
            None, 
            None, 
            None
        )
        assert 1 == len(page.data)

