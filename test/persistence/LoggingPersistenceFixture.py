# -*- coding: utf-8 -*-
"""
    tests.persistence.LoggingPersistenceFixture
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import datetime

from pip_services_commons.log import LogLevel
from pip_services_commons.errors import ErrorDescriptionFactory
from pip_services_commons.data import FilterParams, PagingParams
from pip_services_logging.data.version1 import LogMessageV1

class LoggingPersistenceFixture:
    _persistence = None

    def __init__(self, persistence):
        self._persistence = persistence


    def test_create_messages(self):
        message = self._persistence.create(
            None, 
            LogMessageV1(LogLevel.Info, None, "123", None, "AAA")
        )
        assert None != message

        message = self._persistence.create(
            None, 
            LogMessageV1(LogLevel.Debug, None, "123", None, "BBB")
        )
        assert None != message

        message = LogMessageV1(LogLevel.Error, None, "123", ErrorDescriptionFactory.create(Exception('Test error')), "AAB")
        message.time = datetime.datetime.utcnow() - datetime.timedelta(days=1)
        message = self._persistence.create(
            None, 
            message
        )
        assert None != message


    def test_read_write(self):
        from_time = datetime.datetime.utcnow()

        self.test_create_messages()

        page = self._persistence.get_page_by_filter(
            None, 
            FilterParams.from_tuples("search", "AA"), 
            None
        )
        assert 2 == len(page.data)

        page = self._persistence.get_page_by_filter(
            None, 
            FilterParams.from_tuples("max_level", LogLevel.Info), 
            None
        )
        assert 2 == len(page.data)

        page = self._persistence.get_page_by_filter(
            None, 
            FilterParams.from_tuples("from_time", from_time), 
            None
        )
        assert 2 == len(page.data)


    def test_search(self):
        self.test_create_messages()

        page = self._persistence.get_page_by_filter(
            None, 
            FilterParams.from_tuples("search", "AA"), 
            None
        )
        assert 2 == len(page.data)

        page = self._persistence.get_page_by_filter(
            None, 
            FilterParams.from_tuples("search", "23"), 
            None
        )
        assert 3 == len(page.data)

        page = self._persistence.get_page_by_filter(
            None, 
            FilterParams.from_tuples("search", "rror"), 
            None
        )
        assert 1 == len(page.data)

