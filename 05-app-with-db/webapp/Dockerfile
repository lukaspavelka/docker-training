# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Optional: Add a maintainer label
LABEL maintainer="Lukas Pavelka <your-email@example.com>" # Please replace with your actual email if desired

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Make port 5001 available to the host. Gunicorn will listen on this port.
EXPOSE 5001

# Define environment variable for Flask (though Gunicorn will manage the app)
ENV FLASK_APP=app.py

# Use Gunicorn as the WSGI server for production.
# It's more robust than Flask's built-in development server.
# --bind 0.0.0.0:5001: Listen on all network interfaces within the container on port 5001.
# app:app: Look for an instance of the Flask application named 'app' in the 'app.py' module.
# You might need to add Gunicorn to your requirements.txt if you want to lock its version.
# For this example, we assume Gunicorn is available or can be installed.
# If not in requirements.txt, you'd add `RUN pip install gunicorn` before this.
# For simplicity here, let's add gunicorn to requirements.txt.
# (User should ensure gunicorn is in requirements.txt or install it in a RUN step)
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
