#!/bin/python
# -*- coding: utf-8 -*-

import requests

CITY = "787657"
API_KEY = "c96c759c587a2be4ac68f6116f4b5381"
UNITS = "Metric"
LANG = "en"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))
try:
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))
        print("{}°".format(TEMP))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")
