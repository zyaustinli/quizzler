import requests
import html


parameters = {
    "amount":10,
    "type": "boolean",
    "category": 19
}

response = requests.get(url="http://opentdb.com/api.php", params = parameters)
response.raise_for_status()
question_data = response.json()["results"]
question_data = html.unescape(question_data)