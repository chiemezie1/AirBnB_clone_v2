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


# Define the hosts
env.hosts = ['34.207.61.137', '34.239.255.22']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(archive_no_ext)

        # Create the directory where the archive will be unpacked
        run("mkdir -p {}".format(release_path))

        # Unpack the archive to the created directory
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        # Delete the uploaded archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move the unpacked content to the correct directory
        run("mv {}/web_static/* {}/".format(release_path, release_path))

        # Delete the now-empty web_static directory
        run("rm -rf {}/web_static".format(release_path))

        # Delete the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False
