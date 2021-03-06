# Energy Monitor REST API examples

This is a collection of example Python scripts that demonstrate the usage of the Energy Monitor REST API. 
The REST API itself is accessible via browser (base address is [https://<Energy Monitor Host>/api/](https://<Energy Monitor Host>/api/)).
While Python was chosen for these examples the REST API can be used with other languages or systems too.

## Authentication

The method available for authentication is **JSON Web Token**. The core client functionality is easy to implement and does not
require special packages or code.

## Content negotiation

By default the response content will be delivered as **JSON**.
MessagePack (see [https://msgpack.org/](https://msgpack.org/)) is also available by setting the `Accept` header of the request to `application/msgpack`.

## Examples

### auth_token.py

Obtain and decode a JSON Web Token for authentication.

### increments.py

Load aggregated consumption/generation data of metering devices.

### points.py

Load time series data of metering devices e.g. for x-y Plots.

### meterlog_electrical.py

Upload a set of metrics for an electrical metering devices.

### meterlog_fluid.py

Upload set of metrics for an fluid metering devices.

### meterlog_generic.py

Upload set of metrics for an generic metering devices.

## Disclaimer

The REST API may change without notice. These examples are meant as a rough guideline to get you started and come without any warranty. 