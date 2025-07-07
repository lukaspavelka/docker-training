# Example 2: WordPress Installation with MySQL

This example demonstrates how to set up a WordPress installation using Docker Compose. It includes:
1.  A **WordPress service** running the latest WordPress image (`wordpress:latest`).
2.  A **database service** running MySQL 5.7 (`mysql:5.7`) for WordPress to store its data.

## Files

-   `docker-compose.yml`: Defines the `wordpress` and `db` (MySQL) services.
    -   It includes a healthcheck for the MySQL service.
    -   The WordPress service uses `depends_on` with `condition: service_healthy` to ensure MySQL is ready before WordPress starts.
    -   A named volume `db_data` is used for MySQL data persistence.
-   `README.md`: This file.

## How to Build and Run

1.  **Navigate to this directory (`compose/Example2`) in your terminal.**

2.  **Build (if applicable) and start the services:**
    ```bash
    docker compose up --build
    ```
    -   `--build`: Ensures any local image builds are processed (though both services here use pre-built images from Docker Hub).
    -   To run in detached mode (in the background), add the `-d` flag: `docker compose up --build -d`

3.  **Access WordPress:**
    Open your web browser and go to:
    `http://localhost:8000`

    You should be greeted by the WordPress installation screen. Follow the on-screen instructions to set up your WordPress site (language, site title, admin username, admin password, etc.).

## Database Persistence

The `db` service uses a named volume `db_data` to persist the MySQL database files where WordPress stores all its content. This ensures your WordPress site's data (posts, pages, settings, etc.) remains even if you stop and remove the containers (`docker compose down`). When you next run `docker compose up`, WordPress will connect to the existing data.

To start with a completely fresh WordPress installation (which will also delete all your existing WordPress content):
```bash
docker compose down -v
# OR individually (the volume name might be prefixed by the project directory name):
# docker volume rm example2_db_data
```

## Default Credentials & Security

This example uses the following default credentials for the MySQL database, defined in `docker-compose.yml` for the `db` service:
-   Root Password: `somewordpress`
-   Database Name: `wordpress`
-   User: `wordpress`
-   Password: `wordpress`

These same credentials (user, password, database name) are provided to the `wordpress` service via environment variables so it can connect to the database.

**IMPORTANT:** These are for demonstration purposes only. **NEVER use these default credentials in a production environment.**
For production, use strong, unique passwords and manage them securely, for example, using environment files (`.env`) or Docker secrets. Refer to `compose/howto.txt` for more on this.
The WordPress admin user you create during the WordPress setup screen is separate from these database credentials.

## Troubleshooting

-   If WordPress shows a database connection error:
    -   Ensure both `wordpress` and `db` containers are running (`docker compose ps`).
    -   Check the logs for the `db` container: `docker compose logs db`. MySQL might take some time to initialize, especially on the first run. The healthcheck is designed to help with this.
    -   Verify that the `WORDPRESS_DB_HOST`, `WORDPRESS_DB_USER`, `WORDPRESS_DB_PASSWORD`, and `WORDPRESS_DB_NAME` environment variables for the `wordpress` service in `docker-compose.yml` correctly correspond to the `db` service's settings and name.

## To Stop the Application

1.  If running in the foreground (`docker compose up`), press `Ctrl+C`.
2.  If running in detached mode, or from another terminal:
    ```bash
    docker compose down
    ```
    To also remove the named volume `db_data` (and thus all WordPress data):
    ```bash
    docker compose down -v
    ```
