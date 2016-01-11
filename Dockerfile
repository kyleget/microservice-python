FROM python:2.7-onbuild

LABEL description="Starter template for a Python microservice" \
      version="0.0.1"

MAINTAINER Kyle Getrost <kyle@getro.st>

EXPOSE 5000
CMD python ./myservice/app.py
