import requests

headers = {
    'Accept': '*/*',
    'User-Agent': 'request',
}

url = "http://dummy.restapiexample.com/api/v1/employees"

resposta = requests.get(url, headers=headers)

print(resposta.text)
