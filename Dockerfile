FROM python:3.10

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV FLASK_APP app.py
WORKDIR /project
ADD . /project

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
