# -*- coding: utf-8 -*-
"""
Script entry point.
"""

from dbunlock import unlock_cmd

# pylint: disable=invalid-name
def program():
    return subprocess.call('sudo {}'.format(unlock_cmd()), shell=True)
    
