import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
BASE_URL = 'https://api.themoviedb.org/3'

def MOVIEDB_API_ENDPOINT():
  response = requests.get(url=f'{BASE_URL}/movie/popular', params={'api_key': config['THEMOVIEDB_API_KEY']})
  data = response.json()
  results = data['results']
  return results

def MOVIEDB_API_GENRES():
  response = requests.get(url=f'{BASE_URL}/genre/movie/list', params={'api_key': config['THEMOVIEDB_API_KEY']})
  data = response.json()
  results = data['genres']
  return results

def MOCK_API_ENDPOINT():
  data_API_response = [
    {
      'name': 'Nome',
      'salario': 'Salário',
      'setor': 'Setor',
      'cargo': 'Cargo',
      'contratacao': 'Contratação'
    },
    {
      'name': 'Felipe Curcio',
      'salario': 20000,
      'setor': 'TI',
      'cargo': 'Desenvolvedor front-end',
      'contratacao': 'CLT'
    },
    {
      'name': 'John Doe',
      'salario': 10000,
      'setor': 'TI',
      'cargo': 'Desenvolvedor back-end',
      'contratacao': 'PJ'
    },
    {
      'name': 'Jenny Doe',
      'salario': 20000,
      'setor': 'RH',
      'cargo': 'Gestor de recrutamento e seleção',
      'contratacao': 'CLT'
    },
    {
      'name': 'Johnny Doe',
      'salario': 8000,
      'setor': 'RH',
      'cargo': 'Assistente de departamento de pessoal',
      'contratacao': 'CLT'
    },
    {
      'name': 'Anakin Skywalker',
      'salario': 16000,
      'setor': 'Conselho Jedi',
      'cargo': 'Jedi',
      'contratacao': 'PJ'
    },
    {
      'name': 'Darth Vader',
      'salario': 16000,
      'setor': 'Império',
      'cargo': 'Sith',
      'contratacao': 'PJ'
    },
  ]
  return data_API_response