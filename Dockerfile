FROM python:3.8.10

COPY . /home

WORKDIR /home

RUN pip install -r requirement.txt
