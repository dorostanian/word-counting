FROM python:3.8.10

COPY ./count_it /home/count_it/
COPY ./requirements.txt /home/requirements.txt
COPY ./tests /home/
COPY ./run.sh /home/run.sh
COPY ./test.sh /home/test.sh

WORKDIR /home

RUN pip install -r requirements.txt
RUN chmod +x run.sh
RUN chmod +x test.sh