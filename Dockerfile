# Use the official Python image as the base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ app/

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the entry point for the container
CMD ["python", "app/app.py"]