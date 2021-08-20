#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
URL=$1
curl -sL "$URL" | grep "Allow:" | cut -d ' ' -f 2-
