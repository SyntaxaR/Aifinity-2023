import requests
import json

querystring = input("TEST: ENTRE QUERY STRING: ")
r = requests.get("https://api.bing.microsoft.com/v7.0/images/search?count=10&q="+querystring, headers={"Ocp-Apim-Subscription-Key": "586498b6ed1b4026adad4ee21b800ad7"})
r = requests.post("http://127.0.0.1:8090/", data=r.content)
r = json.loads(r.content)['result']
for i in r:
    print("url: ","https://stemazon-processed.s3.ap-southeast-1.amazonaws.com/"+i+".png")
    print("\n")