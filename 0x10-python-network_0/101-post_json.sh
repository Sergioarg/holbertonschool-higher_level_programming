#!/bin/bash
# Bash script that sends a JSON POST request to a URL.
curl -sH "Content-Type: application/json" -d @"$2" "$1"
