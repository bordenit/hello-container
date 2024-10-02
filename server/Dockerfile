# Use Python 3.13 base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy the Flask app into the container
COPY app.py /app/app.py

# Expose the port for the Flask web server
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]