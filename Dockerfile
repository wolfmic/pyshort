FROM alpine

RUN mkdir -p /opt/pyshort
RUN mkdir -p /var/www/static

WORKDIR /opt/pyshort

ADD . /opt/pyshort/

RUN apk update
RUN apk add tree
RUN apk add python3 nginx
ADD requirements.txt requirements.txt
ADD nginx.conf /etc/nginx/http.d/pyshort.conf

RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt
RUN /opt/venv/bin/pip install pytz --upgrade
RUN /opt/venv/bin/pip install tzdata --upgrade
RUN /opt/venv/bin/python manage.py collectstatic
RUN /opt/venv/bin/python manage.py makemigrations
RUN /opt/venv/bin/python manage.py migrate

ADD ./entrypoint.sh ./entrypoint.sh

EXPOSE 80
ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
