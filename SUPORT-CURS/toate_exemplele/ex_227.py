import requests


# -------------------------
# VERSION 1: simple GET
# -------------------------
url = 'https://www.springer.com'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print(html_content)
else:
    print("Failed to retrieve the webpage")


# -------------------------
# VERSION 2: GET with params
# -------------------------
url = 'https://springer.com/api'

params = {
    'param1': 'value1',
    'param2': 'value2'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print("Failed to retrieve data. Status code:", response.status_code)