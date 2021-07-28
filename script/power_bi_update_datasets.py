# Feature responsavel por atualizar os datasets do power bi, usando o airflow, assim que uma base for atualizada pelo airflow logo em seguida
# este conjunto de codigo sera ativado e atualizando as bases de dados necessarias 

# Bibliotecas que vão ser usadas para a realização da feature
import adal
import requests
import json

# Credenciais que serão utilizadas na atualização do dataset que esta no power BI
client_id = "Passar client ID do power BI"

username = "Username para conectar no power BI"
password = "Password para conectar no power BI"

# Credencias de acesso do lado da microsoft 
authority_url = 'https://login.windows.net/common'
resource_url = 'https://analysis.windows.net/powerbi/api'

# Context client, token e access_tokken para acessarmos o power bi da cyrela
context = adal.AuthenticationContext(authority=authority_url, validate_authority=True, api_version=None)
token = context.acquire_token_with_username_password(resource=resource_url, client_id=client_id, username=username, password=password)
access_token = token.get('accessToken')

# Monta os grupos de requisição
groups_request_url = 'https://api.powerbi.com/v1.0/myorg/groups'
header = {'Authorization': f'Bearer {access_token}'}
groups_request = json.loads(requests.get(url=groups_request_url, headers=header).content)
groups = [d['id'] for d in groups_request['value']]

# Pega a lista de datasets existentes salvos no power bi
for group in groups:
    datasets_request_url = 'https://api.powerbi.com/v1.0/myorg/groups/' + group + '/datasets'
    datasets_request = json.loads(requests.get(url=datasets_request_url, headers=header).content)
    datasets = [d['id'] for d in datasets_request['value']]
    # Procura o dataset expecifico que queremos que seja atualizado (neste caso todos os datasets serao atualizados) #
    for dataset in datasets:
        refresh_url = 'https://api.powerbi.com/v1.0/myorg/groups/' + group + '/datasets/' + dataset + '/refreshes'
        r = requests.post(url=refresh_url, headers=header)