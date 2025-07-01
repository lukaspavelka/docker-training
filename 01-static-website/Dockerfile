# Use a lightweight Nginx image from Docker Hub
FROM nginx:alpine

# Optional: Add a maintainer label
LABEL maintainer="Lukas Pavelka <your-email@example.com>" # Please replace with your actual email if desired

# Remove the default Nginx welcome page to avoid conflicts
RUN rm -rf /usr/share/nginx/html/*

# Copy the static website files from the 'public' directory in the build context
# to the Nginx html directory in the container.
COPY ./public/ /usr/share/nginx/html/

# Expose port 80 to allow traffic to Nginx
EXPOSE 80

# The default command for the nginx:alpine image is to start Nginx.
# However, it's good practice to specify it explicitly, especially for clarity.
# This command starts Nginx in the foreground.
CMD ["nginx", "-g", "daemon off;"]
