#!/bin/bash

cp comitup-demo /usr/local/bin/
cp demoweb /usr/local/bin/

cp comitup-demo.service /etc/systemd/system/
cp demoweb.service /etc/systemd/system/

systemctl enable comitup-demo.service
systemctl start comitup-demo.service
