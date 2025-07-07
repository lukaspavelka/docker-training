# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Optional: Add a maintainer label
LABEL maintainer="Lukas Pavelka <your-email@example.com>" # Please replace with your actual email if desired

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
# This is done first to leverage Docker's build cache.
# If requirements.txt doesn't change, this layer won't be rebuilt.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the pip cache, useful for keeping image size down.
# -r requirements.txt: Install from the given requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (e.g., app.py) into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
# This is the port Flask will run on by default (as specified in app.py or by Flask's default)
EXPOSE 5000

# Define environment variable for Flask
# FLASK_APP tells Flask where to find the application instance.
# FLASK_RUN_HOST=0.0.0.0 makes the server publicly available (within the container's network).
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run app.py when the container launches
# This uses Flask's built-in development server.
# For production, you would typically use a WSGI server like Gunicorn:
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
CMD ["flask", "run"]
