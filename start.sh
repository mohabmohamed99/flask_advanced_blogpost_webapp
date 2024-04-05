#!/bin/bash

pip install gunicorn  # Install gunicorn if not already present

# Start the Gunicorn server, using the environment variable for port
gunicorn app:app -w 1 --log-file -
