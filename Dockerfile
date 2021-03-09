FROM python:3.6-buster
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./
RUN pip install pip-tools && pip-sync
ADD . /code/

CMD ["./main.py"]