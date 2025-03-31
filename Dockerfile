# Start with a Python 3.12 image
FROM python:3.12-slim

# Install Git LFS
RUN apt-get update && apt-get install -y git-lfs && git lfs install
RUN cat /etc/os-release

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory content into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
