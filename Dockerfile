# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY mysite/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY mysite .

EXPOSE 8000

CMD [ "python","manage.py", "runserver", "0.0.0.0:8000"]