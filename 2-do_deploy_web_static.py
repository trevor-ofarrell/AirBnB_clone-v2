#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web
servers, using the function do_deploy"""
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['104.196.135.236 web-01', '35.237.31.37 web-02']


def do_deploy(archive_path):
    new_path = archive_path.split(".")
    if not path.exists(archive_path):
        return False
    try:
        put('versions/archive_path', '/tmp/archive_path')
        run("mkdir -p /data/web_static/releases/{:s}".format(
            new_path))
        run("tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}".format(
            archive_path, new_path))
        run("rm /data/web_static/current")
        run(
            "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}"
            .format(new_path, new_path))
        run("rm -rf /data/web_static/releases/{:s}/web_static".format(
            new_path))
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/{:s} /data/web_static/current"
            .format(new_path))
        return True
    except:
        return False
