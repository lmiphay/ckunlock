# -*- coding: utf-8 -*-

import invoke

from dbunlock import unlock

ns = invoke.Collection()

ns.add_collection(unlock)

