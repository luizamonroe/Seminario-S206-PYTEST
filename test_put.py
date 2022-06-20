import requests

def test_put_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    data = {
        'id': 1,
        'title': 'S206 Pytest',
        'body': 'Executando testes com Pytest',
        'userId': '1'
    }

    post_id = 1

    url = "https://jsonplaceholder.typicode.com/posts/"

    resposta = requests.put(url + str(post_id), headers=headers, data= data)
    resposta_dict = resposta.json()

    if resposta.status_code == 200:
        assert resposta_dict == data
    else:
        assert False