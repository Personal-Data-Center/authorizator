FROM python

COPY run.sh /run.sh

RUN mkdir authorizator

RUN pip3 install django-admin djangorestframework mysqlclient  django-cas-server

CMD ["/run.sh"]
