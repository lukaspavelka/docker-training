# Example 4: HAProxy Load Balancer with Python Web Farm

This example demonstrates how to use HAProxy as a load balancer in front of multiple instances of a Python web application. Docker Compose is used to define and manage the services, showcasing scaling capabilities.

## Files & Structure

-   `docker-compose.yml`:
    -   Defines a `web` service using a Python application (from `web/Dockerfile`). This service is intended to be scaled.
    -   Defines an `haproxy` service using `haproxy:2.4` image. It maps host port 80 to HAProxy's port 80 for application traffic, and host port 7070 to HAProxy's port 70 for the statistics page.
-   `web/`: Contains the source for the simple Python web application.
    -   `Dockerfile`: Builds the Python web application image (using Python 3 and `http.server`).
    -   `index.py`: The Python web server that returns a unique message including its hostname/instance ID.
-   `haproxy/`: Contains the HAProxy configuration.
    -   `haproxy.cfg`: Configuration file for HAProxy. It's set up to balance traffic across instances of the `web` service.
-   `README.md`: This file.

## How to Build and Run

1.  **Navigate to this directory (`compose/Example4`) in your terminal.**

2.  **Build the web service image and start all services:**
    The command below will also scale the `web` service to 3 instances.
    ```bash
    docker compose up --build --scale web=3 -d
    ```
    -   `--build`: Builds the image for the `web` service from its Dockerfile.
    -   `--scale web=3`: Starts 3 instances of the `web` service. You can change `3` to any number.
    -   `-d`: Runs in detached mode.

3.  **Access the Load-Balanced Web Application:**
    Open your web browser and go to `http://localhost:80` (or just `http://localhost`).
    Refresh the page multiple times. You should see the "Hello from Web Server Instance!" message, and the "Hostname", "Instance ID", and "Container IP" details should change as HAProxy distributes your requests to different backend Python application instances.

4.  **Access HAProxy Statistics Page:**
    Open your web browser and go to `http://localhost:7070`.
    You will be prompted for credentials. Use:
    -   User: `user`
    -   Password: `StrongPassword`
    **(IMPORTANT: Change these default credentials in `haproxy/haproxy.cfg` for any real deployment!)**
    The statistics page shows the status of your frontend and backend servers, request counts, etc.

## How It Works

-   **Scaling:** `docker compose up --scale web=N` creates N instances of the `web` service.
-   **Service Discovery:** Docker's embedded DNS allows the `haproxy` service to resolve the service name `web` (defined in `haproxy.cfg` in the `backend` section). Docker DNS will typically provide the IPs of the scaled `web` instances in a round-robin fashion.
-   **Load Balancing:** HAProxy receives requests on port 80 and distributes them to the backend `web` instances (listening on their internal port 8000) based on the `roundrobin` algorithm defined in `haproxy.cfg`.
-   **Health Checks:** HAProxy performs health checks (`option httpchk GET /`) on the backend instances. If an instance fails the health check, HAProxy will stop sending traffic to it.

## To Stop the Application

1.  If running in the foreground, press `Ctrl+C`.
2.  To stop and remove all services (if running detached or from another terminal):
    ```bash
    docker compose down
    ```
    This will stop and remove the `haproxy` and all scaled `web` service containers and the network.
    If you used named volumes (not in this example by default), add `-v` to remove them: `docker compose down -v`.

## Customizing

-   **Number of Web Instances:** Change the number in `--scale web=N`. You might need to adjust the number of `server web_instanceX web:8000 check` lines in `haproxy.cfg` if you are scaling to a very large number and not using more advanced HAProxy features like `server-template` (which would require HAProxy Enterprise or a more complex setup with DNS service discovery). For typical scenarios with a few instances, the current `haproxy.cfg` setup (listing a few servers pointing to the `web` service) should work as Docker DNS handles the resolution.
-   **HAProxy Configuration:** Modify `haproxy/haproxy.cfg` for different load balancing algorithms, ACLs, SSL termination, etc. Remember to restart/recreate the `haproxy` service after changes (`docker compose up -d --no-deps --build haproxy` or `docker compose restart haproxy` if the image itself doesn't need rebuilding).
-   **Web Application:** Modify the Python code in `web/index.py` or the `web/Dockerfile`. Remember to rebuild the `web` image (`docker compose build web` or use `--build` with `up`).
