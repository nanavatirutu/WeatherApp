import requests
import json

API_KEY = "97f62d9728a409b2396cdf97ab691ad5"
URL = "http://api.openweathermap.org/data/2.5/weather?"
URL_forecast = "http://api.openweathermap.org/data/2.5/forecast?"


def getWeatherInCity(city):
	res = requests.get(URL+"APPID="+API_KEY+"&q="+city)
	if (res.status_code==200):
		return json.loads(res.text)['main']['temp'] , json.loads(res.text)['weather'][0]['description'] 



def getForecast(city):
	res = requests.get(URL_forecast+"APPID="+API_KEY+"&q="+city)
	if (res.status_code==200):
		return json.loads(res.text)['list'][7]['main']['temp']
		


