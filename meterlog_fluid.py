import random
import logging
import requests
import pendulum
from auth_token import get_token

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('API example')

HOST = '192.168.2.5'
PROTOCOL = 'http'
KEY = 'user'
TOKEN = 'user'

METER_UID = '6959ea0c-8248-40cf-834c-a5afc51c2af9'

if __name__ == '__main__':
    # Request an auth token.
    # This token can be used for requests until it expires (at the time of this writing tokens expire after 5 minutes).
    token = get_token(PROTOCOL, HOST, KEY, TOKEN)

    # Send a request that creates a set of metrics that represents a measurement for an fluid measuring unit (meter).
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
        'avgMassFlowRate': None,  # Mass flow rate [kg/h]
        'minMassFlowRate': None,  # Minimum mass flow rate in the averaging window [kg/h]
        'maxMassFlowRate': None,  # Maximum mass flow rate in the averaging window [kg/h]
        'avgVolumeFlowRate': None,  # Volume flow rate [m³/h]
        'minVolumeFlowRate': None,  # Minimum volume flow rate in the averaging window [m³/h]
        'maxVolumeFlowRate': None,  # Maximum volume flow rate in the averaging window [m³/h]
        'avgPower': None,  # Power [W]
        'minPower': None,  # Minimum Power in the averaging window [W]
        'maxPower': None,  # Maximum Power in the averaging window [W]
        'avgPressure': None,  # Pressure [bar]
        'minPressure': None,  # Minimum pressure in the averaging window [bar]
        'maxPressure': None,  # Maximum pressure in the averaging window [bar]
        'temperature': random.uniform(0, 100),  # Temperature [°C]
        'temperature2': None,  # Temperature 2 [°C]
        'relHumidity': None,  # Relative humidity [%]
        'dewpoint': None,  # Dew point [°C]
        'totalMass': None,  # Total mass [kg]
        'totalVolume': None,  # Total volume [m³]
        'totalEnergy': None,   # Total energy [Wh]
        'level': None,  # Level reservoir [%]
    }
    response = requests.post(
        f'{PROTOCOL}://{HOST}/api/meterlog/rows/',
        json=payload,
        headers={'Authorization': f'JWT {token}'}
    )
    if response.status_code != 201:
        # The API will respond with error details if possible (e.g. {"timestamp":"Duplicate timestamp."}).
        logger.error('Error response with staus code %s: %r', response.status_code, response.text)
        raise SystemExit
    logger.info('Response status: %s', response.status_code)
    logger.info('Response text: %s', response.text)
