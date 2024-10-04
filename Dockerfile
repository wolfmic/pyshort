FROM alpine

RUN apk add python3 py-pip

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt  --break-system-packages

ENV FLASK_APP app.py
WORKDIR /project
ADD . /project

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
