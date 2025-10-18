import requests, json

url = "https://cholesterol-level-570119871231.europe-west1.run.app"
## if post
r = requests.post(url, json={"LDL": 90, "HDL": 70})
## if get
r = requests.get(url, json={"LDL": 90, "HDL": 70})
print(r.status_code, r.json())