import requests
import json
from . import stockx_search_product



for pg in range(1,15):
    current_bid_url = "https://stockx.com/api/customers/5350379/buying/current?sort=created_at&order=DESC&limit=20&page="+str(pg)+"&currency=USD"
    headers = {
        "cookie":"__cfduid=ddfd3209f8e42948f03a52cd304c424991550723127; cto_lwid=25cd3e97-7c94-4cff-8fb2-1d30ad3ad258; _ga=GA1.2.1759953033.1550723137; _tl_duuid=5f9c40ac-6d2b-49c3-a448-f01b2190a466; tracker_device=e4118d71-7107-4ca1-b16d-8dcf4e268e10; ajs_group_id=null; ajs_anonymous_id=%2227ad7ea2-541a-41ef-816c-0af6df7b257a%22; rskxRunCookie=0; rCookie=czq7h78uwfd1c37algwvsc; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _fbp=fb.1.1550798376047.1194747652; _scid=e4fdca92-2185-4e7a-9a68-5da24ac176f9; _pxvid=dd45f8a1-567a-11e9-800f-6358157ff7d7; intercom-id-h1d8fvw9=a696bbed-4e73-4511-8230-1794021e32b8; IR_gbd=stockx.com; _pxhd=fe8225b5fe6d82142c2db0ee01d485c5ad6cb40701a3c802d04f2d061ca861f5:dd45f8a1-567a-11e9-800f-6358157ff7d7; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_multi_edit_seen=true; _gcl_au=1.1.1645975475.1558564281; stockx_seen_bid_new_info=true; stockx_seen_ask_new_info=true; show_bid_ask_spread=false; show_below_retail=true; stockx_default_sneakers_size=11; stockx_product_visits=17; stockx_homepage=sneakers; _gid=GA1.2.1318498363.1559795729; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1559795732%2C%22https%3A%2F%2Fhelp.stockx.com%2Fcontacting-support%2Fhow-do-i-contact-customer-service%22%5D; _pk_id.421.1a3e=5f7b717bb6731bf0.1557793210.22.1559795732.1559795731.; is_gdpr=false; stockx_selected_currency=USD; stockx_selected_locale=en_US; stockx_user_logged_in=true; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA2IDA0OjM1OjMyIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU2MDQwMDUzMiwiYXBpX2tleXMiOltdfQ.vvBp-hI0Lfn68KmRs4aSJEyZXNrZcegzdpnkOvowS9Q; IR_9060=1559795732662%7C0%7C1559795732662%7C%7C; IR_PI=6ec2deb3-78b1-11e9-9fc0-42010a246302%7C1559882132662; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_bid_education_times=1; mobile_nav_v2=true; multi_edit_option=decrease; product_page_v2=watches%2Chandbags; show_watch_modal=true; cookie_policy_accepted=true; lastRskxRun=1559795805830; intercom-session-h1d8fvw9=VU1CLzlueEdhL1JkeVlaVlhQalRHaFRFbU5xUko4czl4MUVBWCtIQngzeHNIeStrM1ErbU9IQW1YZ2RJKzUxTC0tOVd4Z2dvYnhqeXludURLc0xMQ2lBZz09--774c03195597d3a3eb91ac988752f96d790b6bbd; _sp_id.1a3e=bb58aec7-cccd-4c8e-8a83-adc867c7eb34.1557842726.50.1559807291.1559795851.662b1410-f356-4c70-8f3b-2bda067d6fe7; _sp_ses.1a3e=*; stockx_bid_ask_spread_seen=true",
        "jwt-authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA2IDA0OjM1OjMyIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU2MDQwMDUzMiwiYXBpX2tleXMiOltdfQ.vvBp-hI0Lfn68KmRs4aSJEyZXNrZcegzdpnkOvowS9Q",
        "referer":"https://stockx.com/buying",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    session = requests.session()
    response = session.get(url=current_bid_url,headers=headers,verify=False)
    # print(response.text)

    response_dict = json.loads(response.text)
    for i in response_dict['PortfolioItems']:
        product_title = i['product']['title']
        product_styleId = i['product']['styleId']
        product_shoeSize = i['product']['shoeSize']
        product_amount = i['amount']
        product_parentId = i['product']['parentId']
        product_lowestAsk = i['product']['market']['lowestAsk']
        product_numberOfAsks = i['product']['market']['numberOfAsks']
        product_highestBid = i['product']['market']['highestBid']
        product_numberOfBids = i['product']['market']['numberOfBids']

        stockx_search_product.style_id = product_styleId


        if int(product_amount)<int(product_highestBid):
            print(
                product_title,"\t",
                product_styleId,"\t",
                product_shoeSize,"\t",
                product_amount,"\t",
                product_lowestAsk,"\t",
                product_numberOfAsks,"\t",
                product_highestBid,"\t",
                product_numberOfBids,"\t",
            )