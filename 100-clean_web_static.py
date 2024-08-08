#!/usr/bin/python3
# Fabric script to delete out-of-date archives

from fabric.api import env, run, local
import os

# Define the hosts
env.hosts = ['34.207.61.137', '34.239.255.22']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    
    # Clean local archives
    if number == 0:
        number = 1

    # Get the list of archives in the local versions directory
    local_archives = sorted(
        [f for f in os.listdir('versions') if os.path.isfile(os.path.join('versions', f))],
        reverse=True
    )

    if len(local_archives) > number:
        archives_to_remove = local_archives[number:]
        print(f"Deleting the following local archives: {archives_to_remove}")
        for archive in archives_to_remove:
            local(f"rm versions/{archive}")

    # Clean remote archives
    for host in env.hosts:
        with env.host_string(host):
            # Get the list of remote archives in /data/web_static/releases
            run("ls -1 /data/web_static/releases/ | grep web_static | sort -r > /tmp/archives.txt")
            remote_archives = run("cat /tmp/archives.txt").split()
            
            if len(remote_archives) > number:
                archives_to_remove = remote_archives[number:]
                print(f"Deleting the following remote archives on {host}: {archives_to_remove}")
                for archive in archives_to_remove:
                    run(f"rm -rf /data/web_static/releases/{archive}")
            
            # Remove the temporary file
            run("rm /tmp/archives.txt")
