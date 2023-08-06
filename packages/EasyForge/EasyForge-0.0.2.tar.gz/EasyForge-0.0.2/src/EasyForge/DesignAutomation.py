import requests
from EasyForge.Authentication import Authenticate

def Activities(forge_client_id='', forge_client_secret='', authenticate_scope='code:all'):
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    bucket_url = 'https://developer.api.autodesk.com/oss/v2/buckets'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.post(bucket_url, headers=headers)
    return response.text
