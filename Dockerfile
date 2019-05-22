FROM python:3.6
LABEL version="0.1"
LABEL description="runs"
LABEL maintainer="me@marius.xyz"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY . /opt

WORKDIR  /opt

RUN pip install pipenv
RUN pipenv install --deploy --system

EXPOSE 8000

CMD ["bash", "start.sh", "docker"]
