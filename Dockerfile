FROM continuumio/anaconda3:2020.11

ADD . /code
Workdir /code

ENTRYPOINT ["python", "main.py"]