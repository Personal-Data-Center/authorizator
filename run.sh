#! /bin/sh

cd authorizator
python3 /authorizator/manage.py migrate && python3 /authorizator/manage.py runserver 0.0.0.0:80 > logs.txt
