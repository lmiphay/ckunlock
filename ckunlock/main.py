# -*- coding: utf-8 -*-
"""
Script entry point.
"""

import sys
from ckunlock.dbunlock import unlock_users


def program():
    """ckunlock console script entry point."""
    return unlock_users(sys.argv[2:])
