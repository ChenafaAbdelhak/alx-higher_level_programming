#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sI "$1" | awk -F': ' '/^Allow:/ { print $2 }'
