#!/bin/sh

# Ensure that the environment variables are loaded
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# Run the application
exec "$@"
