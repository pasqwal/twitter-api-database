# base image
FROM python:3.8-slim-buster

# This will create the /code folder and cd into it
WORKDIR /code

# Set up some environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV FLASK_APP wsgi.py
#ENV FLASK_ENV development

# Run a linux command to install some system poackages
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# Copy a file from your local machine to the image
RUN pip install --upgrade pip
COPY requirements-dev.txt /code/requirements-dev.txt

# Another Linux command, here to install our Python dependencies
RUN pip install -r requirements-dev.txt

# Copy our local project source code to /code
COPY . /code


EXPOSE 5000

#CMD ["flask", "run", "--host", "0.0.0.0"]
ENV FLASK_APP wsgi.py
