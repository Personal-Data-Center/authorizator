FROM python

COPY run.sh /run.sh

RUN mkdir authorizator

RUN pip3 install django-admin djangorestframework mysqlclient

RUN pip3 install -e git+https://github.com/jbittel/django-mama-cas.git#egg=django_mama_cas

CMD ["/run.sh"]
