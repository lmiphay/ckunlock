#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Helper to query console kit session information.
"""

from __future__ import print_function
import pprint
import pwd
import subprocess
import sys


class CkSession(object):
    """
    Wrapper around ck-list-sessions - provides a query for active x11 sessions by user (optional).

    Note, that the man page indicates that this should work (but doesn't currently):

        ck-list-sessions --format="session-id,unix-user,display-type"
    """

    def __init__(self, usernames=()):
        """
        ctor
        :param usernames: optional list of usernames to filter results by
        """
        self.session = {}
        self.uid = set([pwd.getpwnam(user).pw_uid for user in usernames])

    def list_sessions(self):
        """
        run ck-list-sessions and build a list of active sessions
        :return: a reference to self
        """
        name = None
        for line in subprocess.check_output('ck-list-sessions').split('\n'):
            if name is None or not line.startswith('\t'):
                name = line.strip(':')
                self.session[name] = {}
            else:
                key_val = line.strip().split('=')
                if len(key_val) == 2:
                    self.session[name][key_val[0].strip()] = key_val[1].strip().strip("'")
        return self

    def show(self):
        """
        dump a list of active sessions (list_sessions must be called before this).
        :return: a reference to self
        """
        for key, value in self.session.iteritems():
            print(key, '=')
            pprint.pprint(value)
        return self

    def is_x11_session(self, session):
        """
        Return True if the x11-display attribute on the specified session is present (non-empty).
        :param session: the name of the session to test
        :return: True if the x11-display attribute on the specified session is present (non-empty)
        """
        return 'x11-display' in self.session[session] and self.session[session]['x11-display'] != ''

    def is_user_session(self, session):
        """
        Return True if the unix-user attribute on the specified session is on the filter user list
        :param session: the name of the session to test
        :return: True if the unix-user attribute on the specified session is on the filter user list
        """
        return len(self.uid) == 0 or int(self.session[session]['unix-user']) in self.uid

    def x11_session(self):
        """
        Generator which yields x11 sessions owned by users on the filter list
        :return: (yields) sessions which are x11 sessions and owned by users on the filter list
        """
        for session in self.session:
            if self.is_x11_session(session) and self.is_user_session(session):
                yield session


if __name__ == "__main__":
    for session_name in CkSession(sys.argv[2:]).list_sessions().x11_session():
        print(session_name)

    sys.exit(0)
