#!/bin/bash

cp comitup-demo /usr/local/bin/
cp demoweb /usr/local/bin/

cp comitup-demo.service /etc/systemd/system/
cp demoweb.service /etc/systemd/system/

echo "echo Configured using Comitup" > /etc/update-motd.d/99-xfooter
chmod 755 /etc/update-motd.d/99-xfooter

systemctl enable comitup-demo.service
systemctl start comitup-demo.service
