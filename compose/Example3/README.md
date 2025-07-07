# Example 3: Nginx Web Server and Redis Service

This example demonstrates a Docker Compose setup with two services:
1.  **`web`**: An Nginx web server serving a simple static HTML page.
2.  **`redis_service`**: A Redis in-memory data store.

The Nginx page is static and does **not** interact with the Redis service in this particular example. The setup is primarily to demonstrate multi-service applications and the scaling capabilities of Docker Compose.

## Files

-   `docker-compose.yml`: Defines the `web` (Nginx) and `redis_service` (Redis) services.
-   `html/index.html`: A simple HTML file served by Nginx.
-   `README.md`: This file.

## How to Run

1.  **Navigate to this directory (`compose/Example3`) in your terminal.**

2.  **Start the services:**
    ```bash
    docker compose up --build -d
    ```
    -   `--build`: Ensures images are built (though these are pre-built Alpine images).
    -   `-d`: Runs in detached mode.

3.  **Access the Nginx web page:**
    Open your web browser and go to `http://localhost:9090`.

4.  **Access Redis (optional, from host via `redis-cli` if installed):**
    Since Redis port `6379` is mapped to the host:
    ```bash
    redis-cli -p 6379
    # Example commands:
    # PING
    # SET mykey "Hello from Docker Redis"
    # GET mykey
    # EXIT
    ```

## Scaling the Redis Service

You can scale the `redis_service` to run multiple instances. For example, to run 3 instances:

```bash
docker compose up -d --scale redis_service=3
```

**Important Considerations for Scaled Redis Instances:**

*   **Port Mapping:** The `docker-compose.yml` maps port `6379` of the `redis_service` container to port `6379` on the host. When you scale `redis_service` using `docker compose up --scale`, **only one** of these instances can successfully bind to host port `6379`. The other instances will still run and be accessible *within Docker's internal network* (e.g., by other containers in the same Docker Compose project), but they won't be directly accessible from your host machine on port `6379` or other automatically assigned sequential host ports based on the `ports` mapping in the YAML.
*   **Accessing Scaled Instances:**
    *   **Internal Access:** Other services within this `docker-compose.yml` (if they were configured to use Redis) could connect to `redis_service:6379`, and Docker's internal DNS and load balancing would distribute requests among the scaled instances.
    *   **External Access (Advanced):** To make multiple scaled Redis instances accessible externally on different host ports, you would typically:
        1.  Remove the `ports` mapping from the `redis_service` in `docker-compose.yml`.
        2.  Use `docker compose run --service-ports --publish <host_port_1>:6379 redis_service` and similar commands for other instances, or use a more complex proxy setup.
        For this example, scaling primarily demonstrates the capability, and direct external access to each scaled Redis instance is not pre-configured.
*   **Data:** By default, the Redis instances are ephemeral (no data persistence). If you uncomment the volume lines in `docker-compose.yml` for `redis_data`, all scaled instances would share the same volume, which is generally **not** what you want for independent Redis data stores. Each would need its own unique named volume, which requires more complex configuration for scaled services.

## Common Docker Compose Commands (V2: `docker compose ...`)

*   **Validate and view configuration:** `docker compose config`
    *   *Shows the final configuration after merging YAML files, environment variables, etc.*
*   **Build or rebuild service images:** `docker compose build <service_name>`
    *   *Builds images defined in `docker-compose.yml` that have a `build` instruction.*
*   **Create and start containers:** `docker compose up`
    *   *Creates and starts all services. Add `-d` for detached mode.*
*   **List running containers for the project:** `docker compose ps`
    *   *Shows the status of your services.*
*   **View logs:** `docker compose logs -f <service_name>`
    *   *Follows logs for a specific service (or all if service_name is omitted).*
*   **Stop services:** `docker compose stop <service_name>`
    *   *Stops running containers without removing them.*
*   **Stop and remove containers, networks:** `docker compose down`
    *   *Use `docker compose down -v` to also remove named volumes.*
*   **Execute a command in a running container:** `docker compose exec <service_name> <command>`
    *   *Example: `docker compose exec web sh`*
*   **Run a one-off command for a service:** `docker compose run <service_name> <command>`
    *   *Creates a new container to run the command.*
*   **List images used:** `docker compose images`
    *   *Shows images associated with your services.*
*   **Pause/Unpause services:** `docker compose pause/unpause <service_name>`
*   **Kill services:** `docker compose kill <service_name>`
*   **View real-time events:** `docker compose events`
