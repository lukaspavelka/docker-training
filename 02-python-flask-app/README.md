# Example 2: Python Flask Application

This example demonstrates how to containerize a simple Python web application built with the Flask framework.

## Files

-   `Dockerfile`: Instructions to build the Docker image. It uses `python:3.9-slim` as a base, sets up a working directory, installs dependencies from `requirements.txt`, copies the application code, and specifies the command to run the Flask development server.
-   `app.py`: A minimal Flask application with a single route that returns "Hello World".
-   `requirements.txt`: Lists the Python dependencies (Flask).

## How to Build

Navigate to this directory (`02-python-flask-app`) in your terminal and run:

```bash
docker build -t python-flask-example .
```

This command builds a Docker image and tags it as `python-flask-example`.

## How to Run

Once the image is built, run it using:

```bash
docker run -d -p 5000:5000 python-flask-example
```

-   `-d`: Runs the container in detached mode.
-   `-p 5000:5000`: Maps port 5000 on your host machine to port 5000 in the container (where Flask is listening).

Open your web browser and go to `http://localhost:5000`. You should see the "Hello from a Python Flask app in Docker!" message.

**Note:** The Dockerfile uses `flask run`, which starts Flask's built-in development server. For production, you would typically use a WSGI server like Gunicorn (as shown in Example 5).

## To Stop the Container

1.  Find the container ID: `docker ps`
2.  Stop the container: `docker stop <container_id>`
3.  Optionally, remove the container: `docker rm <container_id>`
