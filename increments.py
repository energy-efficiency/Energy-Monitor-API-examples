"""
Energy Monitor REST API example for aggregated consumption/generation of metering devices.

Route: https://<HOST>/api/meterlog/increments/

Parameters:
- meterId: Meter ID (repeat or csv - 1,2,3) (required, Integer/String)
- year: Year (required, Integer)
- month: Month (1..12, Integer)
- day: Day (1..31, Integer)
- costs: include costs (Boolean)

If only the `year` parameter is set the response will include values for all months of the given year.
If `year` and `month` are used the  response will include values for all day of the given year and month.
If `year`, `month` and `day` are used the  response will include values for all hours of the given year, month and day.

Example response (JSON) for the meter id `81` and the year `2020`:
{
    "81": {
        "activeEnergyIn": [
            {
                "period": "2678400.0",
                "start": "2020-01-01T00:00:00+01:00",
                "end": "2020-02-01T00:00:00+01:00",
                "increment": 8124.732069359859
            },
            {
                "period": "2505600.0",
                "start": "2020-02-01T00:00:00+01:00",
                "end": "2020-03-01T00:00:00+01:00",
                "increment": 10030.970604422735
            },
            {
                "period": "2674800.0",
                "start": "2020-03-01T00:00:00+01:00",
                "end": "2020-04-01T00:00:00+02:00",
                "increment": 4558.609833494178
            },
            {
                "period": "2592000.0",
                "start": "2020-04-01T00:00:00+02:00",
                "end": "2020-05-01T00:00:00+02:00",
                "increment": 1673.5588504319312
            },
            {
                "period": "2678400.0",
                "start": "2020-05-01T00:00:00+02:00",
                "end": "2020-06-01T00:00:00+02:00",
                "increment": 3314.4367847262183
            },
            {
                "period": "2592000.0",
                "start": "2020-06-01T00:00:00+02:00",
                "end": "2020-07-01T00:00:00+02:00",
                "increment": 4464.309630740783
            },
            {
                "period": "2678400.0",
                "start": "2020-07-01T00:00:00+02:00",
                "end": "2020-08-01T00:00:00+02:00",
                "increment": 5694.889808825101
            },
            {
                "period": "2678400.0",
                "start": "2020-08-01T00:00:00+02:00",
                "end": "2020-09-01T00:00:00+02:00",
                "increment": 4124.417212410946
            },
            {
                "period": "2592000.0",
                "start": "2020-09-01T00:00:00+02:00",
                "end": "2020-10-01T00:00:00+02:00",
                "increment": 2938.974318755674
            },
            {
                "period": "2682000.0",
                "start": "2020-10-01T00:00:00+02:00",
                "end": "2020-11-01T00:00:00+01:00",
                "increment": 2683.6139363825787
            },
            {
                "period": "2592000.0",
                "start": "2020-11-01T00:00:00+01:00",
                "end": "2020-12-01T00:00:00+01:00",
                "increment": 0
            },
            {
                "period": "2678400.0",
                "start": "2020-12-01T00:00:00+01:00",
                "end": "2021-01-01T00:00:00+01:00",
                "increment": 829566.2236968664
            }
        ],
        "activeEnergyOut": [
            {
                "period": "2678400.0",
                "start": "2020-01-01T00:00:00+01:00",
                "end": "2020-02-01T00:00:00+01:00",
                "increment": 0
            },
            {
                "period": "2505600.0",
                "start": "2020-02-01T00:00:00+01:00",
                "end": "2020-03-01T00:00:00+01:00",
                "increment": 0
            },
            {
                "period": "2674800.0",
                "start": "2020-03-01T00:00:00+01:00",
                "end": "2020-04-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2592000.0",
                "start": "2020-04-01T00:00:00+02:00",
                "end": "2020-05-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2678400.0",
                "start": "2020-05-01T00:00:00+02:00",
                "end": "2020-06-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2592000.0",
                "start": "2020-06-01T00:00:00+02:00",
                "end": "2020-07-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2678400.0",
                "start": "2020-07-01T00:00:00+02:00",
                "end": "2020-08-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2678400.0",
                "start": "2020-08-01T00:00:00+02:00",
                "end": "2020-09-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2592000.0",
                "start": "2020-09-01T00:00:00+02:00",
                "end": "2020-10-01T00:00:00+02:00",
                "increment": 0
            },
            {
                "period": "2682000.0",
                "start": "2020-10-01T00:00:00+02:00",
                "end": "2020-11-01T00:00:00+01:00",
                "increment": 0
            },
            {
                "period": "2592000.0",
                "start": "2020-11-01T00:00:00+01:00",
                "end": "2020-12-01T00:00:00+01:00",
                "increment": 824297.491016013
            },
            {
                "period": "2678400.0",
                "start": "2020-12-01T00:00:00+01:00",
                "end": "2021-01-01T00:00:00+01:00",
                "increment": 0
            }
        ]
    }
}
"""

import requests
from pprint import pprint
from auth_token import get_token

HOST = '192.168.2.5'
PROTOCOL = 'https'
KEY = ''
TOKEN = ''

METER_ID = 81
YEAR = 2018

if __name__ == '__main__':
    # Obtain a JSON web token
    token = get_token(PROTOCOL, HOST, KEY, TOKEN)
    # Perform an API request with the token as header (Authorization: JWT <token>)
    response = requests.get(
        f'{PROTOCOL}://{HOST}/api/meterlog/increments/?meterId={METER_ID}&year={YEAR}',
        headers={'Authorization': f'JWT {token}'}
    ).json()
    pprint(response)
