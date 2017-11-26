#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import subprocess
import sys

import invoke
from invoke import task

import cksession

DBUS_COMMAND = 'dbus-send --system --print-reply --dest="org.freedesktop.ConsoleKit"'
UNLOCK_ARG = 'org.freedesktop.ConsoleKit.Session.Unlock'

def unlock_cmd():
    session = '/org/freedesktop/ConsoleKit/{}'.format(cksession.CkSession().list_sessions().x11_session())
    return '{cmd} {session} {unlock_arg}'.format(cmd=DBUS_COMMAND, session=session, unlock_arg=UNLOCK_ARG)

@task
def unlock(ctx):
    session = '/org/freedesktop/ConsoleKit/{}'.format(CkSession().list_sessions().x11_session())
    ctx.sudo(unlock_cmd(), echo=True)

if __name__ == "__main__":
    sys.exit(subprocess.call('sudo {}'.format(unlock_cmd()), shell=True))
