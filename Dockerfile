#FROM ubuntu:22.04

FROM python:3.8-slim

RUN apt-get update && apt-get install -y python3-pip python3-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip3 install -r requirements.txt

# Expose the port Flask is running on
#EXPOSE 5000

# Run the Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
