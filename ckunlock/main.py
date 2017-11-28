# -*- coding: utf-8 -*-
"""
Script entry point.
"""

import subprocess

from dbunlock import unlock_cmd

def program():
    return subprocess.call('sudo {}'.format(unlock_cmd()), shell=True)
