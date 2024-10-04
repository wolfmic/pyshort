FROM alpine

RUN apk add python3 py-pip

COPY requirements.txt /requirements.txt

ENV FLASK_APP=app.py
WORKDIR /project
RUN python -m venv /project/venv
RUN /project/venv/bin/pip install -r /requirements.txt

COPY app.py /project
RUN mkdir -p /project/templates
COPY templates/* /project/templates
COPY entrypoint.sh /project

EXPOSE 5000

ENTRYPOINT ["/bin/sh", "/project/entrypoint.sh"]
