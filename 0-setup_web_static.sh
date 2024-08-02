#!/usr/bin/env bash
# Script that sets up your web servers for deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/test/

echo "Alx software engineering School" > /data/web_static/releases/test/index.html
echo "Alx software engineering School" > /data/web_static/shared/test/index.html

# Create a symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
NGINX_CONFIG="/etc/nginx/sites-available/default"

if ! grep -q "location /hbnb_static" $NGINX_CONFIG; then
    sed -i "/server_name _;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tautoindex off;\n}" $NGINX_CONFIG
fi

# Restart Nginx
service nginx restart

# Exit successfully
exit 0
