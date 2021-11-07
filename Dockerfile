FROM python:3.8.10

COPY ./count_it /home/
COPY ./requirements.txt /home/requirements.txt
COPY ./tests /home/tests

WORKDIR /home

RUN pip install -r requirements.txt
