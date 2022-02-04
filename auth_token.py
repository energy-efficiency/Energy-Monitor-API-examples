
import requests
import logging


logger = logging.getLogger(__name__)


def get_token(protocol: str, host: str, key: str, token: str) -> str:
    """
    Request and return a new JSON Web Token from the Energy Monitor server.
    :param protocol: HTTP or HTTPS (only use HTTPS in production to prevent exposure of credentials)
    :param host: Energy Monitor Hostname
    :param key: Access token uid
    :param token: Access token
    :return: JSON web token
    """
    payload = {
        'key': key,
        'token': token,
    }
    response = requests.post(f'{protocol}://{host}/api/m2m-token-auth/', payload)
    if response.status_code != 200:
        raise IOError(response.text)
    token = response.json()['access']
    return token
