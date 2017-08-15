FROM ubuntu:16.04
MAINTAINER Taras Slyvka

# Base setting 
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && apt-get install -y python-pip python-dev libpq-dev && apt-get clean
RUN apt-get install -y python-setuptools
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev

# Install pip requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project in container
WORKDIR /project
ADD . /project
