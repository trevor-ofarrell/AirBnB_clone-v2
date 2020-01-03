#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static
code="server {
              location / {
        root /data/www;
    }
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}"
testfile="holberton"
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo $testfile >> /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu.ubuntu /data/
echo $data >> /etc/nginx/nginx.conf
service nginx restart
