# Example 1: Simple Static Website with Nginx

This example demonstrates how to serve a basic static website (HTML, CSS, JavaScript) using Nginx in a Docker container.

## Files

-   `Dockerfile`: Instructions to build the Docker image. It uses `nginx:alpine` as the base image, copies the website content from the `public/` directory into the Nginx server path, and exposes port 80.
-   `public/index.html`: A simple HTML file that will be served.

## How to Build

Navigate to this directory (`01-static-website`) in your terminal and run:

```bash
docker build -t static-website-example .
```

This command builds a Docker image and tags it as `static-website-example`.

## How to Run

Once the image is built, run it using:

```bash
docker run -d -p 8080:80 static-website-example
```

-   `-d`: Runs the container in detached mode (in the background).
-   `-p 8080:80`: Maps port 8080 on your host machine to port 80 in the container (where Nginx is listening).

Now, open your web browser and go to `http://localhost:8080`. You should see the "Hello from a Static Website in Docker!" message.

## To Stop the Container

1.  Find the container ID: `docker ps`
2.  Stop the container: `docker stop <container_id>`
3.  Optionally, remove the container: `docker rm <container_id>`
