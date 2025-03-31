FROM python:3.12-slim

# Install Git LFS
RUN apt-get update && apt-get install -y git-lfs && git lfs install

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to leverage caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Now copy the rest of the application
COPY . /app

# Expose Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

