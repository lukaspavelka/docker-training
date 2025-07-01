# ---- Build Stage ----
# Use an official Go image as the builder image.
# Alpine versions are smaller.
FROM golang:1.20-alpine AS builder

# Optional: Add a maintainer label
LABEL maintainer="Lukas Pavelka <your-email@example.com>" # Please replace with your actual email if desired

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go mod and sum files
COPY go.mod ./
# If you have a go.sum file, uncomment the next line
# COPY go.sum ./

# Download all dependencies.
# Dependencies will be cached if the go.mod and go.sum files are not changed.
RUN go mod download
RUN go mod verify

# Copy the source code into the container
COPY . .

# Build the Go application
# -o /app/main: specifies the output binary name and location
# CGO_ENABLED=0: disables Cgo to build a statically-linked binary (important for small scratch/alpine images)
# -ldflags="-s -w": strips debugging information, reducing binary size
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags="-s -w" -o /app/main .

# ---- Production Stage ----
# Use a minimal base image for the production stage.
# Alpine is small and includes basic shell tools.
# For even smaller images, `FROM scratch` can be used if the binary is fully static and self-contained.
FROM alpine:latest

# Optional: Add a maintainer label for the final image
LABEL maintainer="Lukas Pavelka <your-email@example.com>"

# Set the Current Working Directory inside the container
WORKDIR /root/

# Copy the pre-built binary file from the "builder" stage.
COPY --from=builder /app/main .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the executable
# This is the command that will be executed when the container starts.
CMD ["./main"]
