import requests, json 
class Help() :
	def get_help(self):
		message = "**Welcome to Ninjas Chat Bot**\n"
		message += "\n**Field Name**\n"
		message += "`translate` - Translate Languages to English\n"
		message += "`pnr` - Get PNR Status\n"
		message += "`twitter` - Tweet Directly from Zulip\n"
		message += "`search` Place-Name\n"
		message += "`weather` Location\n"
		return message