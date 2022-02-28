FROM python

ADD . /code
Workdir /code

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]