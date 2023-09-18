# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.3.0

WORKDIR /app

# Change back to root user to install dependencies
USER root

# To install packages from PyPI
RUN pip install --no-cache-dir requests rasa

EXPOSE 5055

# Switch back to non-root to run code
USER $user
