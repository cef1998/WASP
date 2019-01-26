import pprint
import requests

p = pprint.PrettyPrinter()
class Weather() :
    def getWeather(self,longAndLat) :
        weatherUrl = 'https://api.darksky.net/forecast/723b2d9f49798b99a6882a2754f778a9/'+longAndLat+'/?exclude=minutely,hourly,daily' 
        r=requests.get(weatherUrl)
        result = r.json()
        return result