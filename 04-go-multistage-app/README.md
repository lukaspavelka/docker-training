# Example 4: Go Application with Multi-Stage Build

This example demonstrates how to build a Go application using a multi-stage Docker build. This technique helps create significantly smaller production images by separating the build environment from the runtime environment.

## Files

-   `Dockerfile`: Defines a two-stage build:
    1.  **Builder Stage (`golang:1.20-alpine AS builder`):** Copies the source code, downloads dependencies, and compiles the Go application into a static binary.
    2.  **Production Stage (`alpine:latest`):** Copies only the compiled binary from the builder stage into a minimal Alpine Linux image.
-   `main.go`: A simple Go HTTP server that listens on port 8080 and responds with a "Hello World" message.
-   `go.mod`: Defines the Go module and its dependencies (though this example has no external dependencies).

## How to Build

Navigate to this directory (`04-go-multistage-app`) in your terminal and run:

```bash
docker build -t go-multistage-example .
```

This command builds a Docker image and tags it as `go-multistage-example`. The resulting image will be small because it only contains the compiled Go binary and the minimal Alpine runtime.

## How to Run

Once the image is built, run it using:

```bash
docker run -d -p 8080:8080 go-multistage-example
```

-   `-d`: Runs the container in detached mode.
-   `-p 8080:8080`: Maps port 8080 on your host machine to port 8080 in the container (where the Go app is listening).

Open your web browser and go to `http://localhost:8080`. You should see the "Hello from a Go app in Docker (multi-stage build)!" message.

## To Stop the Container

1.  Find the container ID: `docker ps`
2.  Stop the container: `docker stop <container_id>`
3.  Optionally, remove the container: `docker rm <container_id>`
