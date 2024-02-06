# Integrated Weather API

This is an API that uses another API's by [OpenWeather](https://openweathermap.org/) and was built using FastAPI. There 3 routes:

- GET /geocoding (returns latitude and longitude of a give city name + state code)
- GET /forecast (Returns weather forecast for the provided longintide and latitude)
- GET /geocoding_and_forecast (This route combine 2 previouse ones and returns weather forecast for a given city name + state code)

## Installation

After cloning this repo to your local machine you need to activate Python virtual environment that can be done using this command where .new_venv is the name for the nvironment. You can use a different name (all commands are for Mac/Linux):

```
python3 -m venv .new_venv
```

After creating your virtual environment you need to activate it
(assuming you are in directory where .new_venv located):

```
source .new_venv/bin/activate
```

Then install all the packages from the requirements.txt using this command:

```
pip install -r requirements.txt
```

## Usage

### API key at OpenWEather

In order to initialize a request to OpenWeather API, you need to have a [API key](https://home.openweathermap.org/api_keys) included as a parameter. If this is missing or generic, you will get a 401 "Invalid API key" error.
This API expects you to have APPID string stored at the _config.py_ file. It should be located in the root directory. Generate your own api key and store it inside config.py as shown below.

#### config.py example

```
APPID = "22e6d9ba99a99c993af9eeb9999b5e50"
```

When config.py was created you can start using this API. Run the serverfrom the root directory with this command:

```
uvicorn api.main:app --reload
```

If everything is fine you will see these line appeared in your terminal:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [18245] using StatReload
INFO:     Started server process [18247]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:62903 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:62903 - "GET /openapi.json HTTP/1.1" 200 OK
```

If you see that server is running without any error, you can check out the API using Swagger docs UI. For this go to http://127.0.0.1:8000/docs

There you suppose to see 3 endpoints:

1.  GET /geocoding

This endpoint returns geocodes (latitude and longitude) for a given city name (Stockholm for example) and state code (SE).

2. GET /forecast

As name suggests, at this endpoint returns a forecast for a given latitude and longitude (which are required parameters). You can also provide some optional parameters like:

- units (Units of measurement. standard/metric/imperial. Metric by default)
- mode (Response format. json/xml. Json by default)
- lang (Language. English "en" by default)
- cnt (Number of timestamps. 10 by default)

More about all the parameters at the [OpenWeather 5 day forecast](https://openweathermap.org/forecast5#limit)

### Swagger/Curl

With Swagger UI, just put in your coordinates, set to true optional parameters you are interested in and get your response, as easy as that!

And if you want to use curl you can use this command while uvicorn server is running:

```
curl -X 'GET' \
  'http://127.0.0.1:8000/geocoding?city=Stockholm&country_code=SE' \
  -H 'accept: application/json'
```

And if you use something like Postman, send GET request to [http://api.openweathermap.org/geo/1.0/direct](http://api.openweathermap.org/geo/1.0/direct) with "q" = "city,country_code", "appid" = "your_api_key" as required parameters.

## Response data

This is how the succesfull response data for /geocoding route is structured:

```
[
    {
        "name": "Stockholm",
        "local_names": {
            "my": "စတော့ဟုမ်းမြို့",
            "kk": "Стокгольм",
            "sr": "Стокхолм",
            "ur": "سٹاکہوم",
            "pt": "Estocolmo",
            "yi": "שטאקהאלם",
            "kv": "Стокгольм",
            "os": "Стокгольм",
            "ko": "스톡홀름",
            "eo": "Stokholmo",
            "be": "Стакгольм",
            "gl": "Estocolmo",
            "an": "Estocolmo",
            "az": "Stokholm",
            "fr": "Stockholm",
            "sv": "Stockholm",
            "ga": "Stócólm",
            "se": "Stockholbma",
            "fy": "Stokholm",
            "hr": "Stockholm",
            "uz": "Stokgolm",
            "hu": "Stockholm",
            "de": "Stockholm",
            "mk": "Стокхолм",
            "sc": "Stoccolma",
            "eu": "Stockholm",
            "el": "Στοκχόλμη",
            "iu": "ᔅᑑᒃᓱᓪᒻ",
            "th": "สตอกโฮล์ม",
            "it": "Stoccolma",
            "mt": "Stokkolma",
            "ht": "Stokolm",
            "fo": "Stokkhólmur",
            "ta": "ஸ்டாக்ஹோம்",
            "es": "Estocolmo",
            "hy": "Ստոքհոլմ",
            "sq": "Stokholmi",
            "ka": "სტოკჰოლმი",
            "is": "Stokkhólmur",
            "tg": "Стокҳолм",
            "ku": "Stokholm",
            "tt": "Стокгольм",
            "sk": "Štokholm",
            "bn": "স্টকহোম",
            "cv": "Стокгольм",
            "oc": "Estocòlme",
            "ug": "Stokgolm",
            "fa": "استکهلم",
            "fi": "Tukholma",
            "ru": "Стокгольм",
            "hi": "स्टॉकहोम",
            "la": "Holmia",
            "bg": "Стокхолм",
            "en": "Stockholm",
            "mr": "स्टॉकहोम",
            "lv": "Stokholma",
            "ar": "ستوكهولم",
            "ca": "Estocolm",
            "da": "Stockholm",
            "wo": "Stokolm",
            "uk": "Стокгольм",
            "cs": "Stockholm",
            "bo": "སི་ཏོག་ཧོ་ལིམ།",
            "zh": "斯德哥爾摩",
            "am": "ስቶኮልም",
            "ja": "ストックホルム",
            "lt": "Stokholmas",
            "ml": "സ്റ്റോക്ക്‌ഹോം",
            "co": "Stoccolma",
            "he": "סטוקהולם",
            "nl": "Stockholm",
            "no": "Stockholm",
            "pl": "Sztokholm"
        },
        "lat": 59.3251172,
        "lon": 18.0710935,
        "country": "SE"
    }
]
```

Succesfull response for /forecast and /geocoding_and_forecast routes:

```
{
    "cod": "200",
    "message": 0,
    "cnt": 10,
    "list": [
        {
            "dt": 1707231600,
            "main": {
                "temp": -3.15,
                "feels_like": -8,
                "temp_min": -3.15,
                "temp_max": -3.13,
                "pressure": 994,
                "sea_level": 994,
                "grnd_level": 989,
                "humidity": 77,
                "temp_kf": -0.02
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 75
            },
            "wind": {
                "speed": 3.8,
                "deg": 93,
                "gust": 6.94
            },
            "visibility": 10000,
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2024-02-06 15:00:00"
        },
        {
            "dt": 1707242400,
            "main": {
                "temp": -2.9,
                "feels_like": -8.37,
                "temp_min": -2.9,
                "temp_max": -2.39,
                "pressure": 993,
                "sea_level": 993,
                "grnd_level": 986,
                "humidity": 75,
                "temp_kf": -0.51
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 83
            },
            "wind": {
                "speed": 4.73,
                "deg": 97,
                "gust": 8.41
            },
            "visibility": 10000,
            "pop": 0.02,
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2024-02-06 18:00:00"
        },
        {
            "dt": 1707253200,
            "main": {
                "temp": -3.06,
                "feels_like": -8.98,
                "temp_min": -3.06,
                "temp_max": -3.01,
                "pressure": 991,
                "sea_level": 991,
                "grnd_level": 982,
                "humidity": 87,
                "temp_kf": -0.05
            },
            "weather": [
                {
                    "id": 600,
                    "main": "Snow",
                    "description": "light snow",
                    "icon": "13n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 5.38,
                "deg": 72,
                "gust": 10.52
            },
            "visibility": 1174,
            "pop": 0.69,
            "snow": {
                "3h": 0.69
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2024-02-06 21:00:00"
        }
        ...
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
