import requests, json 
class Places() :
    def getPlaces(self,query) :
    	api_key = ''  # Enter your API Key
    	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    	compUrl  = url + 'query=' + query +'&key=' + api_key
    	r = requests.get(compUrl) 
    	print(compUrl)
    	result = r.json()
    	return result