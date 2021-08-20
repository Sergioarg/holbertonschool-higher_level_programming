#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response.
URL=$1
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$URL"
