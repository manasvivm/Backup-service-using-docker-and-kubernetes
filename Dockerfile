# Use a base image with Python installed
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the backup script and requirements file into the container

COPY ./requirements.txt /app/requirements.txt
COPY ./upload1.py /app/upload1.py
COPY ./Google1.py /app/Google1.py
COPY ./newupload.txt /app/newupload.txt

# Install any required dependencies for the backup script
RUN pip install --no-cache-dir -r requirements.txt

# Define volume mount point
VOLUME /data

# Set the command to run the backup script
CMD ["python", "upload1.py"]
