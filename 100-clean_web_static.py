#!/usr/bin/python3
""" Cleans deployment"""

from fabric.api import *
import os
from datetime import datetime
import tarfile


env.hosts = ['3.91.84.106', '3.80.230.115']


def do_clean(number=0):
    """ Removes all but given number of archives"""
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
