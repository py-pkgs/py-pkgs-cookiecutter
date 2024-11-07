#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# If the first argument is a flag (starts with '-') or is empty, assume the default command is `chaturbate_poller`
if [ "${1#-}" != "$1" ] || [ -z "$1" ]; then
  set -- python3 -m {{ cookiecutter.__package_slug }} "$@"
fi

# Print the command to the console and execute it with the arguments passed to the entrypoint
echo "Running command:" "$@"
exec "$@"
