import requests

def data_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    dados_pokemon = response.json()
    return dados_pokemon

if __name__ == '__main__':
    dados_pokemon = data_pokemon('ditto') #entre com o pokemon
    print(dados_pokemon)
    print(dados_pokemon['sprites']['front_shiny'])
