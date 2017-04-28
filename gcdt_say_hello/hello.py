# -*- coding: utf-8 -*-
"""A gcdt-plugin which demonstrates how to implement hello world as plugin."""
from __future__ import unicode_literals, print_function

from gcdt import gcdt_signals
from gcdt.gcdt_logging import getLogger


log = getLogger(__name__)


def say_hello(context):
    """say hi.
    :param context: The _awsclient, etc.. say_hello plugin needs the 'user'
    """
    log.debug('This is a sample debug message.')
    print('MoinMoin %s!' % context.get('user', 'to you'))


def say_bye(context):
    """say bye.
    :param context: The _awsclient, etc.. say_hello plugin needs the 'user'
    """
    print('Bye %s. Talk to you soon!' % context.get('user', 'then'))


def register():
    """Please be very specific about when your plugin needs to run and why.
    E.g. run the sample stuff after at the very beginning of the lifecycle
    """
    gcdt_signals.initialized.connect(say_hello)
    gcdt_signals.finalized.connect(say_bye)


def deregister():
    gcdt_signals.initialized.disconnect(say_hello)
    gcdt_signals.finalized.disconnect(say_bye)
