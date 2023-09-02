# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Change back to root user to install dependencies
USER root

# To install packages from PyPI
RUN pip install --no-cache-dir requests rasa

# Switch back to non-root to run code
USER $user
