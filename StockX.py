import requests
import json
from datetime import datetime, timedelta

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "cookie": "__cfduid=ddfd3209f8e42948f03a52cd304c424991550723127; cto_lwid=25cd3e97-7c94-4cff-8fb2-1d30ad3ad258; _ga=GA1.2.1759953033.1550723137; _tl_duuid=5f9c40ac-6d2b-49c3-a448-f01b2190a466; tracker_device=e4118d71-7107-4ca1-b16d-8dcf4e268e10; ajs_group_id=null; ajs_anonymous_id=%2227ad7ea2-541a-41ef-816c-0af6df7b257a%22; rskxRunCookie=0; rCookie=czq7h78uwfd1c37algwvsc; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _fbp=fb.1.1550798376047.1194747652; _scid=e4fdca92-2185-4e7a-9a68-5da24ac176f9; _pxvid=dd45f8a1-567a-11e9-800f-6358157ff7d7; intercom-id-h1d8fvw9=a696bbed-4e73-4511-8230-1794021e32b8; IR_gbd=stockx.com; _pxhd=fe8225b5fe6d82142c2db0ee01d485c5ad6cb40701a3c802d04f2d061ca861f5:dd45f8a1-567a-11e9-800f-6358157ff7d7; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_multi_edit_seen=true; _gcl_au=1.1.1645975475.1558564281; stockx_seen_bid_new_info=true; stockx_seen_ask_new_info=true; is_gdpr=false; stockx_selected_currency=USD; stockx_selected_locale=en_US; stockx_user_logged_in=true; product_page_v2=watches%2Chandbags; show_watch_modal=true; show_bid_ask_spread=false; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_below_retail=true; mobile_nav_v2=true; multi_edit_option=decrease; cookie_policy_accepted=true; stockx_default_sneakers_size=11; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTAxIDAwOjUwOjExIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU1OTk1NTAxMSwiYXBpX2tleXMiOltdfQ.v1y7rAkF536u2VA3h9_xPdeE6kAWer15TRCglDs0SuM; stockx_product_visits=17; stockx_homepage=sneakers; _sp_ses.1a3e=*; _gat=1; lastRskxRun=1559475559020; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1559475559%2C%22https%3A%2F%2Fhelp.stockx.com%2Fcontacting-support%2Fhow-do-i-contact-customer-service%22%5D; _pk_id.421.1a3e=5f7b717bb6731bf0.1557793210.21.1559475559.1559350213.; _pk_ses.421.1a3e=*; _tl_csid=206cb9ca-3916-4469-9670-40ae4eaaeba7; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_n=JTJGYnV5aW5n; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_l_h=aHR0cHMlM0ElMkYlMkZzdG9ja3guY29tJTJGYnV5aW5n; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_l_t=Sm9yZGFuJTIwMSUyMFJldHJvJTIwSGlnaCUyMENhbW8lMjAzTSUyMFNoYWRvdyUyMC0lMjBBQTM5OTMtMDM0; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_l=JTdCJTIyaHJlZiUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGc3RvY2t4LmNvbSUyRmJ1eWluZyUyMiUyQyUyMmhhc2glMjIlM0ElMjIlMjIlMkMlMjJzZWFyY2glMjIlM0ElMjIlMjIlMkMlMjJob3N0JTIyJTNBJTIyc3RvY2t4LmNvbSUyMiUyQyUyMnByb3RvY29sJTIyJTNBJTIyaHR0cHMlM0ElMjIlMkMlMjJwYXRobmFtZSUyMiUzQSUyMiUyRmJ1eWluZyUyMiUyQyUyMnRpdGxlJTIyJTNBJTIySm9yZGFuJTIwMSUyMFJldHJvJTIwSGlnaCUyMENhbW8lMjAzTSUyMFNoYWRvdyUyMC0lMjBBQTM5OTMtMDM0JTIyJTdE; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_v_d=MjAxOS0wNi0wMlQxMSUzQTM5JTNBMTkuMDU5Wg==; IR_9060=1559350213154%7C0%7C1559349981177%7C%7C; IR_PI=6ec2deb3-78b1-11e9-9fc0-42010a246302%7C1559436613154; intercom-session-h1d8fvw9=cG8wd0NqenRaY3p2eERWbXh1Q25tdlN2ZzZFaDFwNDFxakl2VmsrNW1rRGpBYWFrV1MrYWJCSjZYWDd1Nzg3Ui0td09sUWpleE0rejlscHBJMllaM0NTZz09--fa0963b6e4769dc12ff40620e8284a126919e2ec; _tl_auid=5c617a93825e5a00141fc211; _tl_sid=5cf3b569a1e61c02bf7b23f9; _sp_id.1a3e=bb58aec7-cccd-4c8e-8a83-adc867c7eb34.1557842726.48.1559475569.1559455219.ef81ad53-80d0-4dae-a30e-49b97865730f; stockx_bid_ask_spread_seen=true",
    "referer": "https://stockx.com/buying",
    "jwt-authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTAxIDAwOjUwOjExIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU1OTk1NTAxMSwiYXBpX2tleXMiOltdfQ.v1y7rAkF536u2VA3h9_xPdeE6kAWer15TRCglDs0SuM"

}

login_url = "https://stockx.com/api/login"

email = "645748712@qq.com"
password = "sl5862798&1102"

data = {
    "email": email,
    "password": password,
}

session = requests.session()
login_response = session.post(url=login_url, data=data,headers=headers)

for i in range(1, 9):
    history_url = "https://stockx.com/api/customers/5350379/buying/history?sort=matched_with_date&order=DESC&limit=20&page="+str(i)+"&currency=USD"
    headers = {
        "Cookie":"__cfduid=ddfd3209f8e42948f03a52cd304c424991550723127; cto_lwid=25cd3e97-7c94-4cff-8fb2-1d30ad3ad258; _ga=GA1.2.1759953033.1550723137; _tl_duuid=5f9c40ac-6d2b-49c3-a448-f01b2190a466; tracker_device=e4118d71-7107-4ca1-b16d-8dcf4e268e10; ajs_group_id=null; ajs_anonymous_id=%2227ad7ea2-541a-41ef-816c-0af6df7b257a%22; rskxRunCookie=0; rCookie=czq7h78uwfd1c37algwvsc; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _fbp=fb.1.1550798376047.1194747652; _scid=e4fdca92-2185-4e7a-9a68-5da24ac176f9; _pxvid=dd45f8a1-567a-11e9-800f-6358157ff7d7; intercom-id-h1d8fvw9=a696bbed-4e73-4511-8230-1794021e32b8; IR_gbd=stockx.com; _pxhd=fe8225b5fe6d82142c2db0ee01d485c5ad6cb40701a3c802d04f2d061ca861f5:dd45f8a1-567a-11e9-800f-6358157ff7d7; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_multi_edit_seen=true; _gcl_au=1.1.1645975475.1558564281; stockx_seen_bid_new_info=true; stockx_seen_ask_new_info=true; is_gdpr=false; stockx_selected_currency=USD; stockx_selected_locale=en_US; stockx_user_logged_in=true; product_page_v2=watches%2Chandbags; show_watch_modal=true; show_bid_ask_spread=false; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_below_retail=true; mobile_nav_v2=true; multi_edit_option=decrease; cookie_policy_accepted=true; stockx_default_sneakers_size=11; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTAxIDAwOjUwOjExIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU1OTk1NTAxMSwiYXBpX2tleXMiOltdfQ.v1y7rAkF536u2VA3h9_xPdeE6kAWer15TRCglDs0SuM; stockx_product_visits=17; stockx_homepage=sneakers; _sp_ses.1a3e=*; _gat=1; lastRskxRun=1559475559020; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1559475559%2C%22https%3A%2F%2Fhelp.stockx.com%2Fcontacting-support%2Fhow-do-i-contact-customer-service%22%5D; _pk_id.421.1a3e=5f7b717bb6731bf0.1557793210.21.1559475559.1559350213.; _pk_ses.421.1a3e=*; _tl_csid=206cb9ca-3916-4469-9670-40ae4eaaeba7; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_n=JTJGYnV5aW5n; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_l_h=aHR0cHMlM0ElMkYlMkZzdG9ja3guY29tJTJGYnV5aW5n; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_l_t=Sm9yZGFuJTIwMSUyMFJldHJvJTIwSGlnaCUyMENhbW8lMjAzTSUyMFNoYWRvdyUyMC0lMjBBQTM5OTMtMDM0; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_l=JTdCJTIyaHJlZiUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGc3RvY2t4LmNvbSUyRmJ1eWluZyUyMiUyQyUyMmhhc2glMjIlM0ElMjIlMjIlMkMlMjJzZWFyY2glMjIlM0ElMjIlMjIlMkMlMjJob3N0JTIyJTNBJTIyc3RvY2t4LmNvbSUyMiUyQyUyMnByb3RvY29sJTIyJTNBJTIyaHR0cHMlM0ElMjIlMkMlMjJwYXRobmFtZSUyMiUzQSUyMiUyRmJ1eWluZyUyMiUyQyUyMnRpdGxlJTIyJTNBJTIySm9yZGFuJTIwMSUyMFJldHJvJTIwSGlnaCUyMENhbW8lMjAzTSUyMFNoYWRvdyUyMC0lMjBBQTM5OTMtMDM0JTIyJTdE; tl_sopts_206cb9ca-3916-4469-9670-40ae4eaaeba7_p_p_v_d=MjAxOS0wNi0wMlQxMSUzQTM5JTNBMTkuMDU5Wg==; IR_9060=1559350213154%7C0%7C1559349981177%7C%7C; IR_PI=6ec2deb3-78b1-11e9-9fc0-42010a246302%7C1559436613154; intercom-session-h1d8fvw9=cG8wd0NqenRaY3p2eERWbXh1Q25tdlN2ZzZFaDFwNDFxakl2VmsrNW1rRGpBYWFrV1MrYWJCSjZYWDd1Nzg3Ui0td09sUWpleE0rejlscHBJMllaM0NTZz09--fa0963b6e4769dc12ff40620e8284a126919e2ec; _tl_auid=5c617a93825e5a00141fc211; _tl_sid=5cf3b569a1e61c02bf7b23f9; _sp_id.1a3e=bb58aec7-cccd-4c8e-8a83-adc867c7eb34.1557842726.48.1559475569.1559455219.ef81ad53-80d0-4dae-a30e-49b97865730f; stockx_bid_ask_spread_seen=true",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
        "Referer": "https://stockx.com/buying",
        "JWT-Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTAxIDAwOjUwOjExIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3MzE4NDQxMTg2NDIwMTUzNiIsImV4cCI6MTU1OTk1NTAxMSwiYXBpX2tleXMiOltdfQ.v1y7rAkF536u2VA3h9_xPdeE6kAWer15TRCglDs0SuM",

    }
    history = session.get(url=history_url, headers=headers)
    history_content = history.text
    his_json = json.loads(history_content)
    # 页码方面
    # limit = his_json['Pagination']['limit']
    # page = his_json['Pagination']['page']
    # total = his_json['Pagination']['total']
    # lastPage = his_json['Pagination']['lastPage']
    # currentPage = his_json['Pagination']['currentPage']
    # nextPage = his_json['Pagination']['nextPage']
    # prevPage = his_json['Pagination']['prevPage']
    # sort = his_json['Pagination']['sort']
    # order = his_json['Pagination']['order']

    # 内容方面
    for i in range(len(his_json['PortfolioItems'])):
        content_dict = his_json['PortfolioItems'][i]

        time_1 = content_dict['matchedWithDate'].replace("+00:00", ".000Z")
        data_1 = datetime.strptime(time_1, '%Y-%m-%dT%H:%M:%S.%fZ')
        purchase_time = data_1 + timedelta(hours=8)
        purchase_time = purchase_time.strftime("%Y-%m-%d")

        print(
            content_dict['orderNumber'],"\t",
            content_dict['product']['title'],"\t",
            content_dict['product']['styleId'],"\t",
            content_dict['product']['shoeSize'],"\t",
            content_dict['localTotal'],"\t",
            purchase_time,"\t",
            content_dict['Tracking']['number'])
