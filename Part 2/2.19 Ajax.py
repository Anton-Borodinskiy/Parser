import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
response = requests.get(url=url, headers=headers).json()
print(response)

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    "GiveName": "Monero",
    "GetName": "Dash",
    "Sum": 100,
    "Direction": 0
}

url = "https://bitality.cc/Home/GetSum?"
response = requests.get(url=url, headers=headers, params=data).json()
print(response)

