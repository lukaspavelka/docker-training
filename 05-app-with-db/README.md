# Example 5: Application with a Database (Docker Compose)

This example demonstrates a multi-container setup using Docker Compose. It includes a Python Flask web application that connects to a PostgreSQL database.

## Files & Structure

-   `docker-compose.yml`: Defines two services:
    -   `webapp`: Built from the Dockerfile in the `webapp/` directory. It's a Python Flask application.
    -   `db`: Uses the official `postgres:15-alpine` image.
    It also defines a network for the services to communicate and a volume to persist database data.
-   `webapp/`: Contains the source code for the Flask application.
    -   `Dockerfile`: Instructions to build the web application's Docker image. It uses Gunicorn as the WSGI server.
    -   `app.py`: The Flask application. It has a route `/` and a route `/db_status` to check the database connection.
    -   `requirements.txt`: Python dependencies (Flask, psycopg2-binary, Gunicorn).

## How to Build and Run

This example uses Docker Compose to manage the multi-container application.

1.  **Navigate to this directory (`05-app-with-db`) in your terminal.**

2.  **Build and start the services:**
    ```bash
    docker-compose up --build
    ```
    -   `--build`: Forces Docker Compose to build the images (specifically for the `webapp` service) before starting the containers.
    -   You can add `-d` to run in detached mode: `docker-compose up --build -d`

3.  **Access the application:**
    -   The web application will be available at `http://localhost:5001`.
    -   Check the database connection status at `http://localhost:5001/db_status`.

## How It Works

-   **Networking:** Docker Compose creates a default network that allows the `webapp` container to reach the `db` container using the service name `db` as the hostname.
-   **Database Persistence:** The `postgres_data` volume ensures that data stored in the PostgreSQL database persists even if the `db` container is stopped and removed.
-   **Environment Variables:** The `docker-compose.yml` file passes necessary environment variables to both services (e.g., database credentials for both the `db` service to initialize and the `webapp` service to connect).
-   **`depends_on` and `healthcheck`:** The `webapp` service has `depends_on: db` with `condition: service_healthy`. This means `webapp` will wait for the `db` service to report as healthy (via its `healthcheck`) before starting.

## To Stop the Application

1.  If running in the foreground, press `Ctrl+C`.
2.  To stop services (if running detached or in another terminal):
    ```bash
    docker-compose down
    ```
    -   This command stops and removes the containers, network, and (by default) does not remove named volumes. To remove the volume as well, you can use `docker-compose down -v`.

## Accessing Database Directly (Optional)

The `docker-compose.yml` maps the PostgreSQL port `5432` from the `db` container to port `5432` on your host. You can use a database tool like `psql` or pgAdmin to connect to the database directly using:
-   Host: `localhost`
-   Port: `5432`
-   User: `user`
-   Password: `password`
-   Database: `mydatabase`
