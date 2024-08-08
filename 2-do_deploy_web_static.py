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
        print(f"Archive path {archive_path} does not exist.")
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        print(f"Uploading {archive_path} to /tmp/ directory...")
        put(archive_path, "/tmp/")
        print("Upload complete.")

        archive_filename = os.path.basename(archive_path)
        archive_no_ext = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/{}".format(archive_no_ext)

        # Create the directory where the archive will be unpacked
        print(f"Creating directory {release_path}...")
        run("mkdir -p {}".format(release_path))

        # Unpack the archive to the created directory
        print(f"Unpacking archive to {release_path}...")
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        # Delete the uploaded archive from the web server
        print(f"Removing the archive from /tmp/...")
        run("rm /tmp/{}".format(archive_filename))

        # Move the unpacked content to the correct directory
        print(f"Moving unpacked content...")
        run("mv {}/web_static/* {}/".format(release_path, release_path))

        # Delete the now-empty web_static directory
        print(f"Removing empty web_static directory...")
        run("rm -rf {}/web_static".format(release_path))

        # Delete the existing symbolic link
        print(f"Removing existing symbolic link...")
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        print(f"Creating new symbolic link...")
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
