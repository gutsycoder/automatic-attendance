import requests
import json
url=requests.get("https://api.covid19india.org/v4/data.json").text
data=json.loads(url)
print("Confirmed Cases in Lucknow ",data["UP"]["districts"]["Lucknow"]["total"]["confirmed"])
print("Deaths in Lucknow ",data["UP"]["districts"]["Lucknow"]["total"]["deceased"])
print("Recovered in Lucknow ",data["UP"]["districts"]["Lucknow"]["total"]["recovered"])
try:
	print("Today's Cases in Lucknow are",data["UP"]["districts"]["Lucknow"]["delta"]["confirmed"])
except:
	pass
