#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web
servers, using the function do_deploy"""
from fabric.api import *
from os import path

env.hosts = ['104.196.135.236', '35.237.31.37']
env.user = 'ubuntu'


def do_deploy(archive_path):
    new_path = archive_path.split("/")[1].split(".")[0]
    ap = new_path.split(".")[0]
    print(new_path)
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{:s}".format(ap))
        run("tar -xzf /tmp/{:s}.tgz -C /data/web_static/releases/{:s}".format(
            new_path, ap))
        run("rm /data/web_static/current")
        run(
            "mv /data/web_static/releases/{}/web_static/* ".format(ap) +
            "/data/web_static/releases/{}".format(ap))
        run("rm -rf /data/web_static/releases/{:s}/web_static".format(ap))
        if path.exists("/data/web_static/current"):
            run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{:s} /data/web_static/current"
            .format(ap))
        print("New version deployed!")
        return True
    except:
        return False
