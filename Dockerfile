#Pull base image
FROM python:3.8

#Set environment variables
ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

#Set work directory
WORKDIR /online-shop

#Isnstall dependencies
COPY Pipfile Pipfile.lock /online-shop/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/