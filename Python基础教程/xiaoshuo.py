#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import run


def host_type():
    run('free -m')