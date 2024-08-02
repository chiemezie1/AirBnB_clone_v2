#!/usr/bin/python3
# A Fabric script that generates a .tgz archive
#    from the contents of the web_static folder

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(date)
        # tar -zcvf filename path
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None
    finally:
        pass
