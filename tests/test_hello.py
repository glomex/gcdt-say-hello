# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import pytest

from gcdt_say_hello.hello import say_hello, say_bye


def test_hello(capsys):
    context = {'user': 'Stuart'}

    say_hello(context)
    out, err = capsys.readouterr()
    assert out == "MoinMoin Stuart!\n"


def test_hello_no_user(capsys):
    context = {}

    say_hello(context)
    out, err = capsys.readouterr()
    assert out == "MoinMoin to you!\n"


def test_bye(capsys):
    context = {'user': 'Stuart'}

    say_bye(context)
    out, err = capsys.readouterr()
    assert out == "Bye Stuart. Talk to you soon!\n"


def test_bye_no_user(capsys):
    context = {}

    say_bye(context)
    out, err = capsys.readouterr()
    assert out == "Bye then. Talk to you soon!\n"
