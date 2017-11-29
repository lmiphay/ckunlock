#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
DBus based session unlocking
"""

from __future__ import print_function
import subprocess
import sys
import ckunlock.cksession

DBUS_COMMAND = 'dbus-send --system --print-reply --dest="org.freedesktop.ConsoleKit"'
UNLOCK_ARG = 'org.freedesktop.ConsoleKit.Session.Unlock'


def unlock_session(session_name):
    """
    create and return a shell dbus-send command which will unlock a single session
    :param session_name: the name of the session to be unlocked
    :return: the complete shell command to unlock the specified session
    """
    session = '/org/freedesktop/ConsoleKit/{}'.format(session_name)
    return '{cmd} {session} {unlock_arg}'.format(cmd=DBUS_COMMAND, session=session, unlock_arg=UNLOCK_ARG)


def unlock_users(users):
    """
    unlock the x11 sessions belonging to the specified users
    :param users: users whose sessions will be unlocked
    :return: 0 if the operation(s) were successful
    """
    result = 0
    for session in ckunlock.cksession.CkSession(users).list_sessions().x11_session():
        result = result | subprocess.call('sudo {}'.format(unlock_session(session)), shell=True)
    return result


if __name__ == "__main__":
    sys.exit(unlock_users(sys.argv[2:]))
