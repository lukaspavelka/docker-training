# Specify a base image version for reproducibility
FROM ubuntu:22.04

LABEL maintainer="Lukas Pavelka"

# Combine RUN instructions to reduce layers
# Use --no-install-recommends to minimize installed packages
# Clean up apt cache to reduce image size
# Install curl for potential healthchecks or other uses
# Explicitly use python3 and pip3
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
    python3 \
    python3-pip \
    wget \
    curl && \
    pip3 install awscli && \
    rm -rf /var/lib/apt/lists/*

# Copy configuration files
# Assuming these paths are relative to the Docker build context (DockerFile directory)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY sites-enabled/default /etc/nginx/sites-enabled/default

# Copy web content
COPY html /usr/share/nginx/html

# Expose ports (good for documentation and for `docker run -P`)
EXPOSE 80
EXPOSE 443

# Healthcheck to ensure Nginx is running (optional, but recommended)
# This checks every 30 seconds if Nginx is responding on port 80.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost/ || exit 1

# Start supervisord
# Explicitly specify the configuration file for supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
