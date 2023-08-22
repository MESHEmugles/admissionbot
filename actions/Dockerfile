# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.3.0

# Change back to root user to install dependencies
USER root

# To install packages from PyPI
RUN pip install --no-cache-dir requests

# Switch back to non-root to run code
USER $user