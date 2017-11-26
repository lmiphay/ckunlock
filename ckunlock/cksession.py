#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint
import subprocess
import sys

class CkSession(object):
    """
    The man page indicates that:
    ck-list-sessions --format="session-id,unix-user,display-type"
    should work, but doesn't at the moment
    """
    
    def __init__(self):
        self.session = {}

    def list_sessions(self):
        name = None
        for line in subprocess.check_output('ck-list-sessions').split('\n'):
            if name is None or not line.startswith('\t'):
                name = line.strip(':')
                self.session[name] = {}
            else:
                kv = line.strip().split('=')
                if len(kv) == 2:
                    self.session[name][kv[0].strip()] = kv[1].strip().strip("'")
        return self
                
    def show(self):
        for key, value in self.session.iteritems():
            print(key, '=')
            pprint.pprint(value)
        return self

    def x11_session(self):
        for sess in self.session.keys():
            if 'x11-display' in self.session[sess] and self.session[sess]['x11-display'] != '':
                return sess
        return None

if __name__ == "__main__":
    print(CkSession().list_sessions().x11_session())
    
    sys.exit(0)
