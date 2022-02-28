FROM continuumio/anaconda3:2020.11

RUN apt update
RUN apt install mariadb-server
RUN mysql_secure_installation


ADD . /code
Workdir /code

ENTRYPOINT ["python", "main.py"]
