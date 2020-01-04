#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

testfile="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "$testfile" >> /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu.ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
