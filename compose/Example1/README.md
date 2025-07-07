# Example 1: PHP Application with MySQL Database

This example demonstrates a multi-container setup using Docker Compose. It includes:
1.  A **web service** running PHP with Apache (`php:7.2.2-apache` image).
2.  A **database service** running MySQL 5.7 (`mysql:5.7` image).

The PHP application (`index.php`) attempts to connect to the MySQL database and display the connection status, server version, and a list of tables.

## Files

-   `docker-compose.yml`: Defines the `web` (PHP) and `db` (MySQL) services, their configurations, network port mappings, and a named volume (`db_data`) for MySQL data persistence.
-   `php/index.php`: The PHP script that connects to the MySQL database.
-   `README.md`: This file.

## How to Build and Run

1.  **Navigate to this directory (`compose/Example1`) in your terminal.**

2.  **Build and start the services:**
    ```bash
    docker compose up --build
    ```
    -   `--build`: Forces Docker Compose to build the images if they don't exist or if changes were made (though in this case, we are using pre-built images, so it mainly creates the services).
    -   To run in detached mode (in the background), add the `-d` flag: `docker compose up --build -d`

3.  **Access the PHP application:**
    Open your web browser and go to:
    `http://localhost:8100`

    You should see a page indicating the status of the MySQL connection.

## Database Persistence

The `db` service uses a named volume `db_data` to persist the MySQL database files. This means that even if you stop and remove the containers (`docker compose down`), the data will remain in the volume. When you next run `docker compose up`, MySQL will reuse the existing data.

If you want to start with a fresh database, you can remove the volume using:
```bash
docker compose down -v
# OR individually:
# docker volume rm example1_db_data # (The volume name might be prefixed with the project directory name)
```

## Default Credentials & Security

This example uses the following default credentials for the MySQL database, defined in `docker-compose.yml`:
-   Root Password: `my_secret_pw_shh`
-   Database Name: `test_db`
-   User: `devuser`
-   Password: `devpass`

**IMPORTANT:** These are for demonstration purposes only. **NEVER use these default credentials in a production environment.**
For production, use strong, unique passwords and manage them securely, for example, using environment files (`.env`) or Docker secrets. Refer to `compose/howto.txt` for more on this.

## Troubleshooting

-   If `index.php` shows "Connection Failed":
    -   Ensure both `web` and `db` containers are running (`docker compose ps`).
    -   Check the logs for the `db` container: `docker compose logs db`. MySQL might take a moment to initialize.
    -   Verify that the database credentials in `php/index.php` (which attempts to read them from environment variables passed to the `db` service) match those in `docker-compose.yml` for the `db` service.
    -   Ensure the `mysqli` extension is enabled in PHP (it is by default in `php:7.2.2-apache`).

## To Stop the Application

1.  If running in the foreground (`docker compose up`), press `Ctrl+C`.
2.  If running in detached mode, or from another terminal:
    ```bash
    docker compose down
    ```
    To also remove the named volume `db_data`:
    ```bash
    docker compose down -v
    ```
