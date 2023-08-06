import requests
from EasyForge.Authentication import Authenticate


def GetHubs(forge_client_id='', forge_client_secret='', authenticate_scope='data:read'):
    """

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param authenticate_scope: 'data:read'
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    uri = 'https://developer.api.autodesk.com/project/v1/hubs'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(uri, headers=headers)
    return response.text

def GetHubDetails(forge_client_id='', forge_client_secret='',hub_id='', authenticate_scope='data:read'):
    """

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param hub_id: Hub ID
    :param authenticate_scope: 'data:read'
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    uri = f'https://developer.api.autodesk.com/project/v1/hubs/:{hub_id}'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(uri, headers=headers)
    return response.text

def GetHubProjects(forge_client_id='', forge_client_secret='',hub_id='', authenticate_scope='data:read'):
    """

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param hub_id: Hub ID
    :param authenticate_scope: 'data:read'
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    uri = f'https://developer.api.autodesk.com/project/v1/hubs/:{hub_id}/projects'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(uri, headers=headers)
    return response.text

def GetProjectDetails(forge_client_id='', forge_client_secret='',hub_id='', project_id='',
                      authenticate_scope='data:read'):
    """

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param project_id:
    :param hub_id: Hub ID
    :param authenticate_scope: 'data:read'
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    uri = f'https://developer.api.autodesk.com/project/v1/hubs/:{hub_id}/projects/:{project_id}'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(uri, headers=headers)
    return response.text

