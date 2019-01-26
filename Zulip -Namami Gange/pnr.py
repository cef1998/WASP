import requests

class Pnr(object):
	def __init__(self):
		self.ids = {}

	def get_pnr(self, pnrno):
		try:
			print(pnrno)
			json = requests.get("https://api.railwayapi.com/v2/pnr-status/pnr/"+pnrno+"/apikey/ehjli2y8n2/").json()
			passenger = "\n"
			for i in range(0,json["passengers"].__len__()):
				passenger+="**"+str(json["passengers"][i]["no"])+"\t"+json["passengers"][i]["current_status"]+"\t"+json["passengers"][i]["booking_status"]+"**\n"
			message = "PNR Number : **{}**\n From : **{}** - **{}**\n To : **{}** - **{}**\nTrain Name :**{}**\nTrain Number :**{}**\nPassengers:{}".format(pnrno, json["from_station"]["code"],json["from_station"]["name"], json["reservation_upto"]["code"],json["reservation_upto"]["name"],json["train"]["name"],json["train"]["number"],passenger)
			return message
		except KeyError:
			message = "Enter a valid PNR number"
		print(message)
		return message