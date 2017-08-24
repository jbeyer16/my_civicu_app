#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from my_civicu_app.bot import recognize_greeting

__author__ = "Jeff Beyer"
__copyright__ = "Jeff Beyer"
__license__ = "mit"


def test_recognize_greeting():
    assert recognize_greeting('Hi') is True
    assert recognize_greeting('') is False
    # with pytest.raises(AssertionError):
    #     fib(-10)
