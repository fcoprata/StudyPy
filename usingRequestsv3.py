import requests

def response_url(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = response_url('https://web.whatsapp.com/')
    print(response)

    #situação para retirada de texto e leitura