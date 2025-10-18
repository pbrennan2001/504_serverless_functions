import requests

url = f"https://504-serverless-avcvbvhra5g5athh.canadacentral-01.azurewebsites.net/api/http_trigger1?code=LFiTRxfDMlY_1xAP9RVI-gREP33_DS5QoJI5UsNlnx8PAzFuq9lXsA=="

params = {"LDL": 90, "HDL": 70}

print(url, params)

r = requests.post(url, json=params)

print(r.status_code, r.json())