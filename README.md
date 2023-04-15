# airline_rest (simple crud api)

This repository is simple django project which uses rest_framework library and creating a rest api.

## Requirements
* Python 3.10

* Django 3.2

* Django Rest Framework

Simple JWT

Endpoint | HTTP METHOD | Result 
--- | --- | ---
localhost/airline | POST | Creates a new airline 
localhost/airline | GET | List all airline 
localhost/airline/airline_id | GET | Retrieve single airline
localhost/airline/airline_id| PUT | Update the airline object 
localhost/airline/airline_id | DEL | Deletes the airline 
localhost/aircraft | POST | Creates a new aircraft 
localhost/aircraft | GET | List all aircrafts
localhost/aircraft/aircraft_id | GET | Retrieve the aircraft  
localhost/aircraft/aircraft_id | PUT | Update the aircraft 
localhost/aircraft/aircraft_id | DEL | Delete the aircraft 
localhost/api-token-auth | POST | Create the jwt token


## Use

cURL command or PostMan application can be a good choice to make requests
To get to jwt token
```
curl -H "Authorization: JWT YourToken" -d "username=value&password=value" 'http://127.0.0.1:8000/api-auth-token'
````

To get the content with token
```
curl https://112.0.0.1:8000/{required_path}
   -H "Accept: application/json"
   -H "Authorization: Bearer {token}"
```


