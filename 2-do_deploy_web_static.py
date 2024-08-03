#!/usr/bin/python3
# Fabric script to distribute an archive to web servers

from fabric.api import env, put, run
import os

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
        arch_path = "/data/web_static/releases/"
        archive_folder = arch_path + archive_filename.split(".")[0]

        # Create the directory where the archive will be unpacked
        run("mkdir -p {}".format(archive_folder))

        # Unpack the archive to the created directory
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, archive_folder))

        # Delete the uploaded archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move the unpacked content to the correct directory
        run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))

        # Delete the now-empty web_static directory
        run("rm -rf {}/web_static".format(archive_folder))

        # Delete the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(archive_folder))

        return True
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False
