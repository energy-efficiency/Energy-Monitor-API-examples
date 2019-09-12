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

Example response (JSON) for the meter id `81` and the year `2018`:
{
    "81": {
        "activeEnergyIn": {
            "timestamps": [1514761200, 1517439600, 1519858800, 1522533600, 1525125600, 1527804000, 1530396000, 1533074400, 1535752800, 1538344800, 1541026800, 1543618800],
            "increments": [9755.609782625106, 11080.841753489454, 13799.450964572141, 7369.185129176243, 11622.833770880126, 10836.554265822517, 11985.2284609013, 12332.839157918585, 3986.8039737246, 7768.442104256013, 11069.872897322872, 5794.109382405644],
            "valueConfig": {
                "key": "activeEnergyIn",
                "value": "activeEnergyIn",
                "unit": "Wh",
                "unitKey": "Wh",
                "type": "float",
                "integral": null,
                "integralUnit": null,
                "integralUnitKey": null,
                "inOut": false,
                "verboseName": "Wirkenergie Verbrauch",
                "isPointValue": false,
                "isIncrementValue": true,
                "chartType": "line"
            }
        },
        "activeEnergyOut": {
            "timestamps": [1514761200, 1517439600, 1519858800, 1522533600, 1525125600, 1527804000, 1530396000, 1533074400, 1535752800, 1538344800, 1541026800, 1543618800],
            "increments": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "valueConfig": {
                "key": "activeEnergyOut",
                "value": "activeEnergyOut",
                "unit": "Wh",
                "unitKey": "Wh",
                "type": "float",
                "integral": null,
                "integralUnit": null,
                "integralUnitKey": null,
                "inOut": false,
                "verboseName": "Wirkenergie Erzeugung",
                "isPointValue": false,
                "isIncrementValue": true,
                "chartType": "line"
            }
        },
        "reactiveEnergyIn": {
            "timestamps": [1514761200, 1517439600, 1519858800, 1522533600, 1525125600, 1527804000, 1530396000, 1533074400, 1535752800, 1538344800, 1541026800, 1543618800],
            "increments": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "valueConfig": {
                "key": "reactiveEnergyIn",
                "value": "reactiveEnergyIn",
                "unit": "varh",
                "unitKey": "varh",
                "type": "float",
                "integral": null,
                "integralUnit": null,
                "integralUnitKey": null,
                "inOut": false,
                "verboseName": "Blindenergie Verbrauch",
                "isPointValue": false,
                "isIncrementValue": true,
                "chartType": "line"
            }
        },
        "reactiveEnergyOut": {
            "timestamps": [1514761200, 1517439600, 1519858800, 1522533600, 1525125600, 1527804000, 1530396000, 1533074400, 1535752800, 1538344800, 1541026800, 1543618800],
            "increments": [21048.399963589385, 19245.231141870725, 21352.811420234968, 20596.888505721698, 21518.112736916402, 20918.0274685045, 21635.410357121145, 21645.2379371695, 20410.387363461778, 21129.718277289066, 20449.085411444772, 20989.780833048746],
            "valueConfig": {
                "key": "reactiveEnergyOut",
                "value": "reactiveEnergyOut",
                "unit": "varh",
                "unitKey": "varh",
                "type": "float",
                "integral": null,
                "integralUnit": null,
                "integralUnitKey": null,
                "inOut": false,
                "verboseName": "Blindenergie Erzeugung",
                "isPointValue": false,
                "isIncrementValue": true,
                "chartType": "line"
            }
        }
    }
}
"""

import jwt
import pendulum
import requests
from pprint import pprint

HOST = '192.168.2.5'
PROTOCOL = 'https'
USER = 'user'
PASSWORD = 'user'

METER_ID = 81
YEAR = 2018

if __name__ == '__main__':
    # Obtain a JSON web token
    response = requests.post(f'{PROTOCOL}://{HOST}/api/token-auth/', {'username': USER, 'password': PASSWORD}).json()
    token = response['token']
    # Perform an API request with the token as header (Authorization: JWT <token>)
    response = requests.get(
        f'{PROTOCOL}://{HOST}/api/meterlog/increments/?meterId={METER_ID}&year={YEAR}',
        headers={'Authorization': f'JWT {token}'}
    ).json()
    pprint(response)
    # Optionally you can check the expiration date of the token
    expires = jwt.JWT().decode(token, None, False)['exp']
    print(f'Token is valid until {pendulum.from_timestamp(expires)}')
