# Test script: explore the UK Parliament Written Questions API
# Goal: fetch ONE week of Commons written questions and inspect what fields come back.
# Run this in Google Colab (or locally) before writing the full download loop.

import requests
import json

BASE_URL = "https://questions-statements-api.parliament.uk/api/writtenquestions/questions"

params = {
    "tabledWhenFrom": "2024-03-04",  # one week as a test
    "tabledWhenTo": "2024-03-10",
    "house": "Commons",
    "take": 100,                      # check how many actually come back (there may be a max)
    "skip": 0,
}

response = requests.get(BASE_URL, params=params, timeout=30)
print("Status code:", response.status_code)
print("Final URL:", response.url)  # useful for your write-up's API description

data = response.json()

# 1. What does the top level look like?
print("\nTop-level keys:", list(data.keys()))
print("Total results for this week:", data.get("totalResults"))
print("Results returned in this call:", len(data.get("results", [])))

# 2. What does ONE question look like? Print the whole thing.
first = data["results"][0]
print("\nKeys in one result:", list(first.keys()))
print("\nFull first result:")
print(json.dumps(first, indent=2)[:3000])  # truncated so it doesn't flood the screen
