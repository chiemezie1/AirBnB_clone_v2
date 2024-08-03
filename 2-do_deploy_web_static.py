#!/usr/bin/python3
# A Fabric script that distributes an archive to your web servers

from fabric.api import env, put, run
import os

# Define the hosts
env.hosts = ['34.207.61.137', '34.239.255.22']

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    # Extract archive filename from the path and name without extension
    archive_file = archive_path.split("/")[-1]
    archive_name = archive_file.split(".")[0]

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(archive_file))

        # Create the directory where the archive will be uncompressed
        run("mkdir -p /data/web_static/releases/{}/".format(archive_name))

        # Uncompress the archive to the folder
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_file, archive_name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_file))

        # Move contents out of the extracted folder to the release folder
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_name, archive_name))

        # Delete the now-empty web_static directory
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_name))

        # Delete the symbolic link current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new release
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_name))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
