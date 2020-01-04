#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,"""
from datetime import datetime
from fabric.api import *


def do_pack():
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    name = "{}_{}.tgz".format("web_static", dt_string)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {:s} web_static/".format(name))
        local("mv *.tgz versions")
        return "{}/{}".format("versions", name)
    except:
        return None
