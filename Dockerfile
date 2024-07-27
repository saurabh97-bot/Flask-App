# Using the python image from the docker hub
FROM python:3.9-slim

# set the working directory in the container
WORKDIR /app

# Copy all the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified  in requirements.txt
RUN pip install -r requirements.txt

# Make port available to the world outside the container
EXPOSE 5005 5007 5008


# CMD python jinja_temp.py



