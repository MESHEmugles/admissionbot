# Use the official Nginx base image
FROM nginx

# Remove the default Nginx configuration
# RUN rm /etc/nginx/conf.d/default.conf

# Copy your static files to the container
COPY . /usr/share/nginx/html

# Expose the default Nginx port
EXPOSE 80

