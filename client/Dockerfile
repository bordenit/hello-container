# Use Python 3.13 base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Add the script to fetch content from the Flask web server
COPY fetch_content.py /app/fetch_content.py
RUN python3 -m pip install requests && \
    chmod +x /app/fetch_content.py

# Command to run the script
CMD ["python3","/app/fetch_content.py"]