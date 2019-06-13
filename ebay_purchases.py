import requests
import json
from datetime import datetime,timedelta
requests.packages.urllib3.disable_warnings()

ebay_purchased_url = "https://apisd.ebay.com/experience/myebay_buying/v1/purchase_activity"

shipping_No_url = "https://apisd.ebay.com/svcs/services/Shipping/CoreShippingService/v10"

header = {
    "user-agent":"eBayiPhone/5.31.0",
    "authorization":"Bearer v^1.1#i^1#p^3#f^0#r^1#I^3#t^Ul4xMF84OkQ5ODVCNjYxMkNFREUxMUZCRjA3RDBENDAzNkYxMUVCXzNfMSNFXjI2MA==",
    "x-ebay-c-correlation-session":"si=31e7285d168e11d34a92ef3001543b74,sid=m--me.l--purchases",
}


print()

response = requests.get(url=ebay_purchased_url,headers=header,verify=False)

purchase_url_dict = json.loads(response.text)
purchase_content = purchase_url_dict['modules']['PURCHASE_ACTIVITIES']['containers']

def timeformat(time):
    newTime = datetime.strptime(time,"%Y-%m-%dT%H:%M:%S.%fZ") - timedelta(hours=8)
    return newTime.strftime("%Y-%m-%d")

# 购买日期 货号 尺码 价格 物流 seller
for j in purchase_content:
    purchase_cards_list = j['cards']
    for purchase_card in purchase_cards_list:
        purchase_time = purchase_card['__myb']['orderDate']['value']['value']
        purchase_seller = purchase_card['__myb']['sellerName']
        purchase_product = purchase_card['title']['textSpans'][0]['text']
        purchase_price = purchase_card['displayPrice']['value']['value']
        purchase_shipCost = purchase_card['logisticsCost']['textSpans'][0]['text']
        purchase_status = purchase_card['bannerStatus']['textSpans'][0]['text']
        if purchase_shipCost != "Free Shipping" and purchase_shipCost != "+ calculate" and purchase_shipCost != "":
            purchase_price = float(purchase_price) + float(purchase_card['logisticsCost']['value']['value'])
        elif purchase_shipCost != "+ calculate":
            pass
        elif purchase_shipCost != "":
            pass

        print(
            timeformat(purchase_time),"\t",
            purchase_product,"\t",
            purchase_price,"\t",
            purchase_seller,"\t",
            purchase_status
        )

        # for title in purchase_card['title']['textSpans']:
        #     print(title['text'])
            # product_costs =

