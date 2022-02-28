FROM python:latest

ADD . /code
Workdir /code

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

FROM python:latest
RUN apt-get update
RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install mariadb
WORKDIR /flaskProject
CMD ["python", "app.py"]