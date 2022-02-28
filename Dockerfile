FROM continuumio/anaconda3:2020.11

ADD . /code
Workdir /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]