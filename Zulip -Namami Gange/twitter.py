import tweepy
import configparser
import requests
import os

class Twimega(object):
	def __init__(self):
		config = configparser.ConfigParser()
		config.read("twitter.ini")
		x = config["twitter"]
		auth = tweepy.OAuthHandler(x['consumer_key'], x['consumer_secret'])
		auth.set_access_token(x['access_token_key'], x['access_token_secret'])
		self.api = tweepy.API(auth)
		self.stream = x['stream']
	def get(self):
		return self.api.home_timeline()
	def post(self, text):
		return self.api.update_status(text)
	def post_image(self, img, text):
		if img.endswith("jpg"):
			filename = "tmp.jpg"
		elif img.endswith("png"):
			filename = "tmp.png"
		elif img.endswith("gif"):
			filename = "tmp.gif"
		else:
			message = "Tweet Cannot be Posted - Use Image url ends with png/jpg/gif"
			return message
		#print(img)
		request = requests.get(img, stream=True)
		print(request.status_code)
		if request.status_code == 200:
			with open(filename, 'wb') as image:
				for chunk in request:
					image.write(chunk)
			x = self.api.update_with_media(filename, status=text)
			os.remove(filename)
			return x
		else:
			message = "Try Again  !!!!"
			return message