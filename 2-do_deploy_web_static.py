#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy"""
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['104.196.135.236 web-01', '35.237.31.37 web-02']


def do_deploy(archive_path):
    new_path = archive_path.split(".")
    if path.exists(archive_path):
        return False
    try:
        local("tar -xfv" )
        local("rm /data/web_static/current")
        local("ln -s /data/web_static/releases/new_path /data/web_static/current")
        return True
    except:
        return False
