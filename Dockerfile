FROM python:3.11-alpine

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password dromanov

USER dromanov
