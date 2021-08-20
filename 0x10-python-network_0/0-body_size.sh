#!/bin/bash
# Displays the size of the body of the response.
URL=$1
curl -sI $URL | grep "Content-Length" | awk '{print $2}'
