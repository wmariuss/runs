FROM python:3.6
LABEL author="Marius Stanca"
LABEL mail="me@marius.xyz"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY . /opt/

WORKDIR  /opt

RUN pip install pipenv
RUN pipenv install --deploy --system

CMD ["bash", "start.sh"]
