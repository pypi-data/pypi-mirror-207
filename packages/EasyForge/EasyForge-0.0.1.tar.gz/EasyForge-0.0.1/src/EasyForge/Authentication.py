import requests
import json

def Authenticate(forge_client_id='', forge_client_secret='',
                 authenticate_scopes='', grant_type='client_credentials'):
    """

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param authenticate_scopes: 'data:read data:write viewables:read bucket:create bucket:read bucket:delete'
    :param grant_type: Forge App grant type.
    :return: Forge App Access Token with required/provided scope.
    """
    auth_url = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {'client_id': forge_client_id, 'client_secret': forge_client_secret, 'grant_type': grant_type,
              'scope': authenticate_scopes}
    response = requests.post(auth_url, headers=headers, data=params)
    access_token = json.loads(response.text)['access_token']
    return access_token
