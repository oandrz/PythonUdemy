import requests

query_param = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}
response = requests.get(url="https://opentdb.com/api.php", params=query_param)
response.raise_for_status()
data = response.json()
question_data = data["results"]



