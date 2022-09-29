from contextlib import contextmanager
from typing import Any, Generator

from django.test import LiveServerTestCase

class SeleniumTestCaseBase:
    browsers: Any = ...
    browser: Any = ...
    @classmethod
    def import_webdriver(cls, browser: Any): ...
    def create_webdriver(self): ...

class SeleniumTestCase(LiveServerTestCase):
    implicit_wait: int = ...
    selenium: Any
    @contextmanager
    def disable_implicit_wait(self) -> Generator[None, None, None]: ...
