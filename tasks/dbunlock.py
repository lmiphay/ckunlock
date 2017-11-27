# -*- coding: utf-8 -*-

import invoke
from invoke import task

import dbunlock

@task(default=True)
def unlock(ctx):
    ctx.sudo(dbunlock.unlock_cmd(), echo=True)
