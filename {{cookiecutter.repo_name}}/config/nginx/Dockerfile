# Set nginx base image
FROM nginx

# File Author / Maintainer
MAINTAINER {{ cookiecutter.author_name }}

RUN rm /etc/nginx/conf.d/*.conf

# Copy custom configuration file from the current directory
COPY ./config/nginx/sites/*.conf /etc/nginx/conf.d/
