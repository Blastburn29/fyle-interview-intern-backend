# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Configuring virtual environment
RUN pip install virtualenv
RUN virtualenv env --python=python3.8

# Activate the virtual environment and install dependencies (I have windows machine hence my activate file is in Scripts folder)
RUN . env/Scripts/activate
RUN  pip install --no-cache-dir -r requirements.txt

# Command to start the server using a bash script
CMD ["bash", "run.sh"]