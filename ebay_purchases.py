import requests


ebay_purchased_url = "https://apisd.ebay.com/experience/myebay_buying/v1/purchase_activity"

header = {
    "user-agent":"eBayiPhone/5.31.0",
    "authorization":"Bearer v^1.1#i^1#f^0#r^1#I^3#p^3#t^Ul4xMF85OjE0QThDMzcwRjcwMkM3NzE2Q0M3Nzg1MDMyM0RGMUQwXzNfMSNFXjI2MA==",
    "accept":"application/json;presentity=split"
    # "":"",
    # "":"",
}

response = requests.get(url=ebay_purchased_url,headers=header)

print(response.status_code)