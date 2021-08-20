#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response.
URL=$1
curl -sI "$URL" | grep "Allow:" | cut -d ' ' -f 2-
