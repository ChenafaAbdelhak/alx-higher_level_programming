#!/usr/bin/env bash
# sends a request to an URL given as argument
curl -s "$1" | wc -c
