# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080 for the Flask app
EXPOSE 8080

# Start the Flask application
CMD ["python", "run.py"]