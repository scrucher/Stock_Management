FROM python:3.8

# Copy requirements first for better caching
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip3 install -r /requirements.txt

# Set working directory
WORKDIR /api

# Copy the rest of the application code
COPY . .

# Default command to run the Flask server
RUN flask run