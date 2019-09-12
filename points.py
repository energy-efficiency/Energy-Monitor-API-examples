"""
Energy Monitor REST API example for timestamp value tuples (time series data) of metering devices (e.g. for x-y Plots)

Route: https://<HOST>/api/meterlog/points/

Parameters:
- meterId: Meter ID (repeat or csv - 1,2,3) (required, Integer/String)
- start: Filter by POSIX timestamp
- end: Filter by POSIX timestamp
- values: Measure value keys (automatic if omitted)
- resampling: Timebase in minutes (allows downsampling of the time series)
- compressed: Return compressed data points if true

{
    "1805": {
        "points": [
            [1568153700, 131.00169372558594],
            [1568154600, 131.1643524169922],
            [1568155500, 130.51100158691406],
            [1568156400, 130.29788208007812],
            [1568157300, 130.66578674316406],
            [1568158200, 131.614990234375],
            [1568159100, 129.8009796142578],
            [1568160000, 130.89964294433594],
            [1568160900, 138.88973999023438],
            [1568161800, 129.9112091064453],
            [1568162700, 132.75164794921875],
            [1568163600, 130.7436981201172],
            [1568164500, 141.7407989501953],
            [1568165400, 129.97157287597656],
            [1568166300, 131.65489196777344],
            [1568167200, 131.01731872558594],
            [1568168100, 130.3689727783203],
            [1568169000, 130.38381958007812],
            [1568169900, 130.63265991210938],
            [1568170800, 130.89085388183594],
            [1568171700, 129.82208251953125],
            [1568172600, 130.46885681152344],
            [1568173500, 131.06979370117188],
            [1568174400, 131.53680419921875],
            [1568175300, 129.51275634765625],
            [1568176200, 132.02980041503906],
            [1568177100, 131.63548278808594],
            [1568178000, 130.26905822753906],
            [1568178900, 201.69894409179688],
            [1568179800, 378.1451416015625],
            [1568180700, 376.0704040527344],
            [1568181600, 381.67572021484375],
            [1568182500, 363.51483154296875],
            [1568183400, 374.78228759765625],
            [1568184300, 375.95367431640625],
            [1568185200, 376.4735412597656],
            [1568186100, 382.0111083984375],
            [1568187000, 386.6896667480469],
            [1568187900, 367.28094482421875],
            [1568188800, 343.9930725097656],
            [1568189700, 343.84832763671875],
            [1568190600, 341.06365966796875],
            [1568191500, 338.5739440917969],
            [1568192400, 340.5635070800781],
            [1568193300, 335.7566223144531],
            [1568194200, 342.908203125],
            [1568195100, 338.4752197265625],
            [1568196000, 334.83966064453125],
            [1568196900, 336.2991027832031],
            [1568197800, 333.40155029296875],
            [1568198700, 338.3882751464844],
            [1568199600, 336.2987365722656],
            [1568200500, 337.4253845214844],
            [1568201400, 335.7353210449219],
            [1568202300, 335.4468078613281],
            [1568203200, 340.8451232910156],
            [1568204100, 337.94598388671875],
            [1568205000, 339.7388610839844],
            [1568205900, 342.49041748046875],
            [1568206800, 345.1415710449219],
            [1568207700, 336.1462707519531],
            [1568208600, 339.6264343261719],
            [1568209500, 337.6641540527344],
            [1568210400, 337.5052795410156],
            [1568211300, 341.55853271484375],
            [1568212200, 319.3427429199219],
            [1568213100, 313.6667785644531],
            [1568214000, 229.17303466796875],
            [1568214900, 197.1361846923828],
            [1568215800, 189.1825408935547],
            [1568216700, 186.02297973632812],
            [1568217600, 186.83859252929688],
            [1568218500, 185.91452026367188],
            [1568219400, 190.62527465820312],
            [1568220300, 181.96324157714844],
            [1568221200, 178.1931610107422],
            [1568222100, 178.61767578125],
            [1568223000, 178.81605529785156],
            [1568223900, 178.36207580566406],
            [1568224800, 178.70372009277344],
            [1568225700, 177.59701538085938],
            [1568226600, 178.4150848388672],
            [1568227500, 178.3162078857422],
            [1568228400, 178.2562713623047],
            [1568229300, 177.699462890625],
            [1568230200, 177.9681396484375],
            [1568231100, 177.86000061035156],
            [1568232000, 178.38494873046875],
            [1568232900, 177.8794708251953],
            [1568233800, 178.6839599609375],
            [1568234700, 177.58230590820312],
            [1568235600, 177.74290466308594],
            [1568236500, 178.0853271484375],
            [1568237400, 178.51573181152344],
            [1568238300, 178.30233764648438]
        ],
        "valueConfigs": [{
            "key": "avgActivePwr",
            "value": "avgActivePwr",
            "unit": "W",
            "unitKey": "W",
            "type": "float",
            "integral": "activeEnergyIn",
            "integralUnit": "Wh",
            "integralUnitKey": "Wh",
            "inOut": true,
            "verboseName": "Wirkleistung",
            "isPointValue": true,
            "isIncrementValue": false,
            "chartType": "area"
        }],
        "queryTime": 0.0014541299999990542,
        "compressionTime": null,
        "time": 0.001685890000000967,
        "isCompressed": false
    }
}
"""

import pendulum
import requests
from pprint import pprint

HOST = '192.168.2.5'
PROTOCOL = 'http'
USER = 'user'
PASSWORD = 'user'

METER_ID = 1805

if __name__ == '__main__':
    # Obtain a JSON web token
    token = requests.post(
        f'{PROTOCOL}://{HOST}/api/token-auth/', {'username': USER, 'password': PASSWORD}
    ).json()['token']
    # Perform an API request with the token as header (Authorization: JWT <token>)
    yesterday = pendulum.now().subtract(days=1).start_of('day')
    start = yesterday.int_timestamp
    end = yesterday.end_of('day').int_timestamp
    response = requests.get(
        f'{PROTOCOL}://{HOST}/api/meterlog/points/?meterId={METER_ID}&start={start}&end={end}',
        headers={'Authorization': f'JWT {token}'}
    ).json()
    pprint(response)
