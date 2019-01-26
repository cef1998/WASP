import pprint
import zulip
import sys
import re
import json
from weather import Weather 
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload
from chatterbot import ChatBot
from translate import Translate
from twitter import Twimega
from pnr import Pnr
from geocode import Geocode
p = pprint.PrettyPrinter()
BOT_MAIL = "myra-bot@saharsh.zulipchat.com"

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://saharsh.zulipchat.com/api/")
		self.subscribe_all()
		self.trans = Translate()
		self.tw = Twimega()
		self.pnr = Pnr()
		self.weather = Weather()
		self.geo = Geocode()
						
		print("Initialization Done ...")
		self.subkeys = ["crypto", "translate", "define", "joke", "weather", 
				"giphy", "pnr", "mustread", "poll", "hackernews", "hn", "HN", "motivate",
				"twitter", "screenshot", "memo", "cricnews", "help", "shorturl"]

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def process(self, msg):
		content = msg["content"].split()
		sender_email = msg["sender_email"]
		ttype = msg["type"]
		stream_name = msg['display_recipient']
		stream_topic = msg['subject']

		print(content)

		if sender_email == BOT_MAIL:
			return 

		print("Sucessfully heard.")

		if content[0].lower() == "ninjas33" or content[0] == "@**ninjas33**":
			if content[1].lower() == "translate":
				ip = content[2:]
				ip = " ".join(ip)
				message = self.trans.translate(ip)

				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
			if content[1].lower() == "pnr":
				message = self.pnr.get_pnr(content[2])
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
			
			if content[1].lower() == "twitter":
				if len(content) > 2 and content[2] == "post":
					if self.tw.stream == msg["display_recipient"]:
						status = self.tw.post(" ".join(content[3:]))
						x = json.dumps(status._json)
						x = json.loads(x)
						message = "https://twitter.com/{}/status/{}".format(x["user"]["screen_name"], x["id_str"])
						message = "Tweet Posted\n" + message
						self.client.send_message({
							"type": "stream",
							"subject": msg["subject"],
							"to": msg["display_recipient"],
							"content": message
							}) 
					else:
						message = "Use the stream **{}** to post a tweet".format(self.tw.stream)
						self.client.send_message({
							"type": "stream",
							"to": sender_email,
							"content": message
							})
						
			if len(content) > 2 and content[2] == "post_image":
					if self.tw.stream == msg["display_recipient"]:
						status = self.tw.post_image(content[3], " ".join(content[4:]))
						if isinstance(status, str):
							message = status
						else:
							x = json.dumps(status._json)
							x = json.loads(x)
							message = "https://twitter.com/{}/status/{}".format(x["user"]["screen_name"], x["id_str"])
							message = "Tweet Posted\n" + message
						self.client.send_message({
							"type": "stream",
							"subject": msg["subject"],
							"to": msg["display_recipient"],
							"content": message
							}) 
					else:
						message = "Use the stream **{}** to post a tweet".format(self.tw.stream)
						self.client.send_message({
							"type": "private",
							"to": sender_email,
							"content": message
							})

			if content[1].lower() == "weather":
				place = " ".join(content[2:])
				try:
					result = self.weather.getWeather(self.geo.convert(place))
					message = "**"+"Weather update of "+place+"**"+"\n"+"Summary : " + "**"+result["currently"]["summary"]+"**"+"\n"+"Temparature : " +"**"+ str(result["currently"]["temperature"])+"**" +'\n'+"Apparent Temparature : "+"**"+str(result["currently"]["apparentTemperature"])+"**"+"\n"+"Dew Point : "+"**"+str(result["currently"]["dewPoint"])+"**"+"\n"+"Humidity : "+"**"+str(result["currently"]["humidity"])+"**"			
				except KeyError:
					message = "Not Working Right Now"
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message  
				})
					
			if content[1] not in self.subkeys:
				ip = content[1:]
				ip = " ".join(ip)
				message = self.chatbot.get_response(ip).text
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})

		
		elif "ninjas33" in content and content[0] != "ninjas33":
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "Hey there! :blush:"
				})
		else:
			return

def main():
	bot = ZulipBot()
	bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Thanks for using ninja33bot Bot. Bye!")
		sys.exit(0)
