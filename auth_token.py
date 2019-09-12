import jwt
import requests
import pendulum
import logging

logger = logging.getLogger(__name__)


def get_token(protocol: str, host: str, username: str, password: str) -> str:
    """
    Request and return a new JSON Web Token from the Energy Monitor server.
    :param protocol: HTTP or HTTPS (only use HTTPS in production to prevent exposure of credentials)
    :param host: Energy Monitor Hostname
    :param username: Username
    :param password: Password
    :return: JSON web token
    """
    payload = {
        'username': username,
        'password': password,
    }
    response = requests.post(f'{protocol}://{host}/api/token-auth/', payload)
    if response.status_code != 200:
        raise IOError(response.text)
    token = response.json()['token']
    # The token can be decoded to extract information (e.g. expiration time)
    # This step is optional, you do not need special packages or code to use JSON Web Tokens.
    expires = jwt.JWT().decode(token, None, False)['exp']
    logging.info('Token is valid until %s.', pendulum.from_timestamp(expires))
    return token
