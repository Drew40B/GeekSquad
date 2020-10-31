FROM python

WORKDIR  /code

RUN pip install debugpy

copy ./src /code

CMD ["python","-m","debugpy","--listen","localhost:3000","--wait-for-client","hello.py" ]