# Environment

Make pg container:

`docker run --name pg -e POSTGRES_PASSWORD=123456 -p 5432:5432 --mount source=pg_data,target=/var/lib/postgresql/data -d postgres:9.6.9-alpine`


Run/stop pg container:
* Start: `docker start pg`
* Stop: `docker stop pg`


## Starting dev version
With pipenv activated, inside the project folder.

* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser`



# API

Intended for communitcation between front and back end.

## [*GET*] Usage data 
URL: `api/<water||power>/usage/<day||month>/<unix_timestamp>`

### Response:
```json
{
	"data": [123, 42, 213, ...],
	"units": "kwH",
}
```
### Description 
`data` is an ordered array of data for either a day or a month. For a day - it's 24 values, 1 for each hour. In case of month - it represents each day in a calendar month. Values can be both integer and floats.

Notes: only data for a specific day is supported right now. Monthly data will come when Half-Life 3 comes out...



## [*GET*] Retrieve threshold information

URL: `api/<water||power>/threshold`

### Response: 

```json
{
    "threshold": 14
}
```
### Description 
Returns the threshold for either water or power, depending on the URL.



## [*GET*] Retrieve status of all appliances
URL: `api/appliance/`

### Response
```json
[
    {
        "id": "12341dsa12dq",
        "name": "Appliance name",
        "type": "Appliance type"
        "data": {
            "value": 123,
            "unit": "C",
            "description": "Some description of value"
        }
    }, ...
]
```