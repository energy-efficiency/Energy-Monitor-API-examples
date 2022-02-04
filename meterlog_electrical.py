import random
import logging
import requests
import pendulum
from auth_token import get_token

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('API example')

HOST = 'localhost:8181'
PROTOCOL = 'http'
KEY = 'cfd50064-61b0-4394-819e-495b978cd8bd'
TOKEN = 'Wb1wV009q0NhLE5LuAOGgr9xe3KSAyeq'

METER_UID = '6959ea0c-8248-40cf-834c-a5afc51c2af9'

if __name__ == '__main__':
    # Request an auth token.
    # This token can be used for requests until it expires (at the time of this writing tokens expire after 5 minutes).
    token = get_token(PROTOCOL, HOST, KEY, TOKEN)

    # Send a request that will create a set of metrics that represents a measurement for an electrical measuring unit (meter).
    # The timestamp will be rounded to log interval precision (e.g. 15 minutes).
    # Timestamp and meter id have to be unique together. The API will response with an status code 400
    # if a log entry with the same timestamp (after rounding) already exists for the meter.
    # In this case you should discard the log entry (do not send it again as it will fail repeatedly).
    # The optional measures (the ones not marked as required) can be omitted from the payload or set to `None`.
    payload = {
        # Unique meter id (required)
        'meter_uid': METER_UID,
        # POSIX timestamp [s] or ISO 8601/RFC 3339 (required)
        # Please use a timezone aware format (e.g. "2018-06-30T18:30:00+02:00") or use UTC timezone (e.g. 1530376200)
        'timestamp': pendulum.now().isoformat(),
        'avgActivePwr': random.uniform(0, 100),  # Average active power (required) [W]
        'minActivePwr': None,  # Minimum active power in the averaging window [W]
        'maxActivePwr': None,  # Maximum active power in the averaging window [W]
        'avgReactivePwr': None,  # Average reactive power [var]
        'minReactivePwr': None,  # Minimum reactive power in the averaging window [var]
        'maxReactivePwr': None,  # Maximum reactive power in the averaging window [var]
        'activeEnergyIn': random.uniform(0, 1000),  # Total active energy in (required) [Wh]
        'activeEnergyOut': None,  # Total active energy out [Wh]
        'reactiveEnergyIn': None,  # Total reactive energy in [varh]
        'reactiveEnergyOut': None,  # Total reactive energy out [varh]
    }
    response = requests.post(
        f'{PROTOCOL}://{HOST}/api/meterlog/rows/',
        json=payload,
        headers={'Authorization': f'JWT {token}', }
    )
    if response.status_code != 201:
        # The API will respond with error details if possible (e.g. {"timestamp":"Duplicate timestamp."}).
        logger.error('Error response with staus code %s: %r', response.status_code, response.text)
        raise SystemExit
    logger.info('Response status: %s', response.status_code)
    logger.info('Response text: %s', response.text)
