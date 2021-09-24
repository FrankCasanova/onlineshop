#Pull base image
FROM python:3.8

#Set environment variables
ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

#Set work directory
WORKDIR /onlineshop

#Isnstall dependencies
COPY Pipfile Pipfile.lock /onlineshop/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /onlineshop/