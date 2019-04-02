#
# Training Dockerfile
#
FROM ubuntu:latest
MAINTAINER Lukas Pavelka "lukas.pavelka@gmail.com"

USER root

ENV http_proxy 'http://172.16.3.3:3128'
ENV https_proxy 'http://172.16.3.3:3128'
RUN apt-get update && apt-get install -y -q --no-install-recommends ca-certificates wget && apt-get clean 

RUN apt-get update
RUN apt-get install -y nginx nodejs

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory
ADD nginx.conf /etc/nginx/

ADD web /usr/share/nginx/html/

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 8080

# Set the default command to execute
# when creating a new container
CMD service nginx start
