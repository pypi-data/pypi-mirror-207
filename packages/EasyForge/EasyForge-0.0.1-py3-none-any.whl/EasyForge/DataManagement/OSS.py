import json
import os
import requests
from EasyForge.Authentication import Authenticate


def CreateBucket(forge_client_id='', forge_client_secret='', bucket_key='', authenticate_scope='bucket:create',
                 x_ads_region='us', policyKey='transient'):
    """
    The method will create bucket in Forge Aps.

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param bucket_key: Key/ Name
    :param authenticate_scope: 'bucket:create'
    :param x_ads_region: 'us', Area Region
    :param policyKey: Data retention policy. Acceptable values: transient, temporary, persistent
    :return: Creating Bucket and Bucket data /response.
    """

    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    uri = 'https://developer.api.autodesk.com/oss/v2/buckets'
    headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json',
               'x-ads-region': x_ads_region}
    params = {'bucketKey': bucket_key, 'policyKey': policyKey}
    response = requests.post(uri, headers=headers, data=json.dumps(params))
    return response.text


def DeleteBucket(forge_client_id='', forge_client_secret='', bucket_key='', authenticate_scope='bucket:delete'):
    """
    The method will delete bucket in Forge Aps.

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param bucket_key: Bucket Key/ Name
    :param authenticate_scope: 'bucket:delete'
    :return: Deleting Bucket and Bucket data /response.
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scope)
    uri = 'https://developer.api.autodesk.com/oss/v2/buckets/' + bucket_key
    headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
    response = requests.delete(uri, headers=headers)
    return response.text


def UploadObjects(forge_client_id='', forge_client_secret='', bucket_key='', file_object=r'',
                  authenticate_scopes='data:write data:create'):
    """

    :param forge_client_id: Forge App Client ID
    :param forge_client_secret: Forge App Secret ID
    :param bucket_key: Bucket Key/ Name
    :param file_object: object/File path
    :param authenticate_scopes: "data:write data:create"
    :return:
    """
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    object_name = os.path.basename(file_object)
    uri = f'https://developer.api.autodesk.com/oss/v2/buckets/{bucket_key}/objects/{object_name}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/octet-stream',
        # 'Content-Length': str(len(file_content))
    }
    with open(file_object, 'rb') as file:
        response = requests.put(uri, headers=headers, data=file)
        return response.text


def UploadSignedS3(forge_client_id='', forge_client_secret='', bucket_key='', file_object=r'',
                   authenticate_scopes='data:write data:create'):
    access_token = Authenticate(forge_client_id=forge_client_id, forge_client_secret=forge_client_secret,
                                authenticate_scopes=authenticate_scopes)
    object_key = os.path.basename(file_object)
    # Step :1 Get Url
    uri = f'https://developer.api.autodesk.com/oss/v2/buckets/{bucket_key}/objects/{object_key}/signeds3upload'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    with open(file_object, 'rb') as file:
        response = requests.get(uri, headers=headers, data=file)
        url_token = json.loads(response.text)['urls'][0]
        uploadKey = json.loads(response.text)['uploadKey']
        # return response.text

    # Step 2 Upload file by url
    headers = {
        'Content-Type': 'application/octet-stream'
    }
    with open(file_object, 'rb') as file:
        response = requests.put(url_token, data=file, headers=headers)
    # upload_header = response.headers.get('ETag')
    # return response.text

    # Step 3 Complete Upload
    url = f'https://developer.api.autodesk.com/oss/v2/buckets/{bucket_key}/objects/{object_key}/signeds3upload'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        # 'x-ads-meta-Content-Type': 'application/octet-stream'
    }
    params = {
        "uploadKey": uploadKey,
        # "eTags": [
        #     upload_header
        # ]
    }
    # print(upload_header, uploadKey)
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.text
