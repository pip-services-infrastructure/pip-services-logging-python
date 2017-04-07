# -*- coding: utf-8 -*-
"""
    tests.persistence.test_LoggingMemoryPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_logging.persistence.LoggingMemoryPersistence import LoggingMemoryPersistence
from .LoggingPersistenceFixture import LoggingPersistenceFixture

class TestLoggingMemoryPersistence:
    persistence = None
    fixture = None

    @staticmethod
    def setup_class(cls):
        cls.persistence = LoggingMemoryPersistence()
        cls.fixture = LoggingPersistenceFixture(cls.persistence)
    
    def setup_method(self, method):
        self.persistence.clear(None)

    def test_read_and_write(self):
        self.fixture.test_read_write()

    def test_search(self):
        self.fixture.test_search()
