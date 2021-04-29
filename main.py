import requests
import json
res = requests.get("https://www.yad2.co.il/realestate/forsale?city=2650&neighborhood=189&property=1,11,25,3,4,49,51,6,7&propertyGroup=apartments")
res_json=json.loads(res.text)
#print(res_json['feed']['feed_items'][0])
print(res_json)
#print(res.status_code)
#print(res.headers['content-type'])