import requests

def dados_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    #print(response.status_code) deve dar 200 se estiver correto
    print(response.json())
    dados = response.json()
    print(dados['logradouro'])
    print(dados['bairro'])


if __name__ == '__main__':
    dados_cep('61940040')