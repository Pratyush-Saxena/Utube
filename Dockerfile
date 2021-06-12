# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV HOST=0.0.0.0:8080

# create root directory for our project in the container
RUN mkdir /Utube

# Set the working directory to /music_service
WORKDIR /Utube

# Copy the current directory contents into the container at /music_service
ADD . /Utube/

EXPOSE 8080

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt