import requests
import json
from datetime import datetime,timedelta
requests.packages.urllib3.disable_warnings()

headers = {
        "Cookie":"__cfduid=ddfd3209f8e42948f03a52cd304c424991550723127; cto_lwid=25cd3e97-7c94-4cff-8fb2-1d30ad3ad258; _ga=GA1.2.1759953033.1550723137; _tl_duuid=5f9c40ac-6d2b-49c3-a448-f01b2190a466; tracker_device=e4118d71-7107-4ca1-b16d-8dcf4e268e10; ajs_group_id=null; ajs_anonymous_id=%2227ad7ea2-541a-41ef-816c-0af6df7b257a%22; rskxRunCookie=0; rCookie=czq7h78uwfd1c37algwvsc; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _fbp=fb.1.1550798376047.1194747652; _scid=e4fdca92-2185-4e7a-9a68-5da24ac176f9; _pxvid=dd45f8a1-567a-11e9-800f-6358157ff7d7; intercom-id-h1d8fvw9=a696bbed-4e73-4511-8230-1794021e32b8; IR_gbd=stockx.com; _pxhd=fe8225b5fe6d82142c2db0ee01d485c5ad6cb40701a3c802d04f2d061ca861f5:dd45f8a1-567a-11e9-800f-6358157ff7d7; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_multi_edit_seen=true; _gcl_au=1.1.1645975475.1558564281; stockx_seen_bid_new_info=true; stockx_seen_ask_new_info=true; show_bid_ask_spread=false; show_below_retail=true; stockx_default_sneakers_size=11; stockx_product_visits=17; stockx_homepage=sneakers; lastRskxRun=1559475559020; intercom-session-h1d8fvw9=cG8wd0NqenRaY3p2eERWbXh1Q25tdlN2ZzZFaDFwNDFxakl2VmsrNW1rRGpBYWFrV1MrYWJCSjZYWDd1Nzg3Ui0td09sUWpleE0rejlscHBJMllaM0NTZz09--fa0963b6e4769dc12ff40620e8284a126919e2ec; _gid=GA1.2.1318498363.1559795729; _sp_ses.1a3e=*; _tl_csid=581c0700-ddef-4fe6-b61a-25dffe4913fa; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1559795732%2C%22https%3A%2F%2Fhelp.stockx.com%2Fcontacting-support%2Fhow-do-i-contact-customer-service%22%5D; _pk_id.421.1a3e=5f7b717bb6731bf0.1557793210.22.1559795732.1559795731.; _pk_ses.421.1a3e=*; _sp_id.1a3e=bb58aec7-cccd-4c8e-8a83-adc867c7eb34.1557842726.49.1559795732.1559476349.4e12d912-3338-40e3-88c1-c618fd7d636c; tl_sopts_581c0700-ddef-4fe6-b61a-25dffe4913fa_p_p_n=JTJGYnV5aW5n; tl_sopts_581c0700-ddef-4fe6-b61a-25dffe4913fa_p_p_l_h=aHR0cHMlM0ElMkYlMkZzdG9ja3guY29tJTJGYnV5aW5n; tl_sopts_581c0700-ddef-4fe6-b61a-25dffe4913fa_p_p_l_t=U3RvY2tYJTNBJTIwQnV5JTIwYW5kJTIwU2VsbCUyMFNuZWFrZXJzJTJDJTIwU3RyZWV0d2VhciUyQyUyMEhhbmRiYWdzJTJDJTIwV2F0Y2hlcw==; tl_sopts_581c0700-ddef-4fe6-b61a-25dffe4913fa_p_p_l=JTdCJTIyaHJlZiUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGc3RvY2t4LmNvbSUyRmJ1eWluZyUyMiUyQyUyMmhhc2glMjIlM0ElMjIlMjIlMkMlMjJzZWFyY2glMjIlM0ElMjIlMjIlMkMlMjJob3N0JTIyJTNBJTIyc3RvY2t4LmNvbSUyMiUyQyUyMnByb3RvY29sJTIyJTNBJTIyaHR0cHMlM0ElMjIlMkMlMjJwYXRobmFtZSUyMiUzQSUyMiUyRmJ1eWluZyUyMiUyQyUyMnRpdGxlJTIyJTNBJTIyU3RvY2tYJTNBJTIwQnV5JTIwYW5kJTIwU2VsbCUyMFNuZWFrZXJzJTJDJTIwU3RyZWV0d2VhciUyQyUyMEhhbmRiYWdzJTJDJTIwV2F0Y2hlcyUyMiU3RA==; tl_sopts_581c0700-ddef-4fe6-b61a-25dffe4913fa_p_p_v_d=MjAxOS0wNi0wNlQwNCUzQTM1JTNBMzEuODg4Wg==; is_gdpr=false; cookie_policy_accepted=true; stockx_selected_currency=USD; stockx_selected_locale=en_US; _gat=1; stockx_user_logged_in=true; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA2IDA0OjM1OjMyIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU2MDQwMDUzMiwiYXBpX2tleXMiOltdfQ.vvBp-hI0Lfn68KmRs4aSJEyZXNrZcegzdpnkOvowS9Q; IR_9060=1559795732662%7C0%7C1559795732662%7C%7C; IR_PI=6ec2deb3-78b1-11e9-9fc0-42010a246302%7C1559882132662; _tl_auid=5c617a93825e5a00141fc211; _tl_sid=5cf8981559eb3e0019bd4925; _pxff_tm=1; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_bid_education_times=1; mobile_nav_v2=true; multi_edit_option=decrease; product_page_v2=watches%2Chandbags; show_watch_modal=true; stockx_bid_ask_spread_seen=true",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
        "Referer": "https://stockx.com/buying",
        "JWT-Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA2IDA0OjM1OjMyIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU2MDQwMDUzMiwiYXBpX2tleXMiOltdfQ.vvBp-hI0Lfn68KmRs4aSJEyZXNrZcegzdpnkOvowS9Q",
    }
url = "https://stockx.com/api/customers/5350379/buying/current?sort=created_at&order=DESC&limit=20&page=1&currency=USD"
requests.packages.urllib3.disable_warnings()
session = requests.session()
# res = session.get(url=url,headers=headers)
# print(res.text)




# style_id = "jordan 7"
# # search_url = "https://gateway.stockx.com/api/v2/search?facets=%5B%22product_category%22%5D&page=0&query="+style_id+"&currency=USD"
search_url = "https://xw7sbct9v6-1.algolianet.com/1/indexes/products/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=XW7SBCT9V6&x-algolia-api-key=6bfb5abee4dcd8cea8f0ca1ca085c2b3"
#
# headers = {
#     "x-api-key":"99WtRZK6pS1Fqt8hXBfWq8BYQjErmwipa3a0hYxX",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
#     "cookie": "_pxhd=ca64fe41d20b48ea4ab2ce0bf4372d653f12ca805cfa60410a5f754c1a34ad0c:9159bb31-8793-11e9-92aa-618a224a0898; __cfduid=d33562a1a4356b0ff1aefc3c5ad5fb69f1559740347",
#     # "x-anonymous-id": "8accbad1-f5cf-4b7f-8b59-c5c4ba96f029",
#     "jwt-authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiaW9zIiwiYXBwX3ZlcnNpb24iOiIzLjEyLjEuMjE3NjUiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA1IDEzOjEyOjI4IiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA4MzcyOTI5Mzg1MDg5NTIzMCIsImV4cCI6MTU2MDM0NTE0OCwiYXBpX2tleXMiOltdfQ.jMr3GbYScMYt-fLTh9aMAlZUZ6wyp09Az9Q8pa6yH3E"
# }
#
form_data = {
    "params":"query=jordan%207&facets=*&filters="
}
#
#
#
# object_ID = ""
# # session = requests.session()
res1 = session.post(url=search_url,data=form_data)
print(res1.text)



# def get_url_content(url,session):
#     return session.get(url=url,headers=headers,verify=False).text
#
# for i in json.loads(get_url_content(search_url,session))['hits']:
#     object_ID = i['objectID']
#
#
# product_detail_url = "https://gateway.stockx.com/api/v2/products/"+object_ID+"?includes=market,360&currency=USD"
# product_detail_dict = json.loads(get_url_content(product_detail_url,session))['Product']
# for key,value in product_detail_dict['children'].items():
#
#     product_detail_shoeSize = value['shoeSize']
#     if float(product_detail_shoeSize) <=13:
#         product_detail_lowestAsk = value['market']['lowestAsk']
#         product_detail_numberOfAsks = value['market']['numberOfAsks']
#         product_detail_highestBid = value['market']['highestBid']
#         product_detail_numberOfBids = value['market']['numberOfBids']
#         print(
#             float(product_detail_shoeSize),"\t",
#             product_detail_lowestAsk,"\t",
#             product_detail_numberOfAsks,"\t",
#             product_detail_highestBid,"\t",
#             product_detail_numberOfBids,"\t",
#               )
