#!/usr/bin/env python

# Importing requests library
import requests

#
import json







# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))
