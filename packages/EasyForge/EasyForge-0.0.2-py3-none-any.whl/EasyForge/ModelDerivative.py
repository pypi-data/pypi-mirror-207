import requests
import json, base64
from EasyForge.Authentication import Authenticate


def EncodeUrn(urn):
    urn_key = str(urn)
    urn_key_bytes = urn_key.encode('ascii')
    base64_urn = base64.b64encode(urn_key_bytes)
    base64_urn_str = base64_urn.decode('ascii')
    return base64_urn_str

def TranslateUrn(forge_client_id='', forge_client_secret='', urn='',
                 authenticate_scopes='data:write data:create data:read', region="US", x_ads_force='false'):
    """

    :param forge_client_id:
    :param forge_client_secret:
    :param urn:
    :param authenticate_scopes:
    :param region: 'us'
    :param x_ads_force: 'true' / 'false'
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/job'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'x-ads-force': x_ads_force
    }

    encodedUrn = EncodeUrn(urn)

    params = {
        "input": {
            "urn": encodedUrn
        },
        "output": {
            "destination": {
                "region": region
            },
            "formats": [
                {
                    "type": "svf",
                    "views": [
                        "3d",
                        "2d"
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.text


def GetManifest(forge_client_id='', forge_client_secret='', urn='',
                authenticate_scopes='data:read'):
    """

    :param forge_client_id:
    :param forge_client_secret:
    :param urn:
    :param authenticate_scopes: 'data:read viewables:read'
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    print(access_token, 'getProperties')
    url = f'https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/manifest'
    headers = {
        'Authorization': f'Bearer {access_token}'
        # 'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.text


def GetMetadata(forge_client_id='', forge_client_secret='', urn='',
                authenticate_scopes='data:read'):
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    url = f'https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/metadata'
    headers = {
        'Authorization': f'Bearer {access_token}'
        # 'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.text


def GetHierarchy(forge_client_id='', forge_client_secret='', urn='', modelGuid='',
                 authenticate_scopes='data:read'):
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    url = f'https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/metadata/{modelGuid}'

    headers = {
        'Authorization': f'Bearer {access_token}'
        # 'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.text


def GetProperties(forge_client_id='', forge_client_secret='', urn='', modelGuid='',
                  authenticate_scopes='data:read'):
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    url = f'https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties'

    headers = {
        'Authorization': f'Bearer {access_token}'
        # 'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.text


def GetThumbnail(forge_client_id='', forge_client_secret='', urn='', modelGuid='',
                 authenticate_scopes='data:read viewables:read'):
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    url = f'https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties'

    headers = {
        'Authorization': f'Bearer {access_token}'
        # 'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.text
