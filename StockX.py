import requests
import json
from datetime import datetime, timedelta
import pymysql

headers = {
        "Cookie":"__cfduid=dfd76c45e1883c7d42b80a201bac831b51561868162; _ga=GA1.2.1832067962.1561868165; _gcl_au=1.1.128188731.1561868166; _tl_duuid=f1f870cd-8e23-4477-8acb-64da02de2dbc; ajs_group_id=null; ajs_anonymous_id=%22e9f04751-f2d9-487c-9337-6dfd15d7adf6%22; cto_lwid=dd71613a-3c2b-49e3-982b-453bd620e5c9; tracker_device=81c60c70-477f-4fa8-b415-c8771605b625; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _fbp=fb.1.1561868169481.1792539972; rskxRunCookie=0; rCookie=cjdyo4h4x4qdbqgoh1xx4; _scid=7927340b-f078-46c1-ae8a-fcca8e5eb5c6; _pxhd=f4f1b1adb700c1c29570b3bd25d6e32d99538142d4a26d434db7b65a80f69b2a:f2ea3270-b08e-11e9-b75c-4d5e1258ff9a; _ALGOLIA=anonymous-6b13d3b1-3f0a-4a78-9eaa-06095f13109b; stockx_session=137x8jylrw9kd1564246361965; stockx_multi_edit_seen=true; IR_gbd=stockx.com; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_seen_bid_new_info=true; stockx_product_visits=7; stockx_default_sneakers_size=All; stockx_homepage=sneakers; is_gdpr=false; stockx_selected_currency=USD; stockx_selected_locale=en_US; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_bid_education_times=1; multi_edit_option=decrease; product_page_v2=watches%2Chandbags; show_watch_modal=true; _derived_epik=dj0yJnU9M0tnOTU0eXpOb3loeUoxUG1uU2twdXl5MC1LTVJ5QmQmbj1jSTR1clJibGM3eWlKMC1KNk9JYzB3Jm09NyZ0PUFBQUFBRjFFYkZJ; stockx_user_logged_in=true; cookie_policy_accepted=true; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA4LTAyIDE3OjA1OjQ1IiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic25lYWtlcnMiLCJpc19hZG1pbiI6IjAiLCJzZXNzaW9uX2lkIjoiMTMxMjIyMTU1MzE0Mzc2MjI2MzEiLCJleHAiOjE1NjUzNzAzNDUsImFwaV9rZXlzIjpbXX0.af-2Iu0Qj12s-sZ9K1L824lV4vtLqveDcoTZGkdMycE; stockx_learn_more_dismiss=true; lastRskxRun=1564901573932; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1564901574%2C%22https%3A%2F%2Fmail.qq.com%2F%22%5D; IR_9060=1564765820473%7C0%7C1564765263562%7C%7C; IR_PI=c8d7e781-9aed-11e9-9801-42010a246302%7C1564852220473; intercom-session-h1d8fvw9=WmhHdlRUSHJGRUt4ZWd5UjBzZFhIZTMzVHRjYWduSHBWNlkrQmd1YVhlVjl1cXNmMG5lV0lCUGppQnQ1eHE2ay0tc0JjSjQvZWN6eWt0YmFPTkt6TjVxUT09--fda681775ae6d42c5f6d69a7770142f448a8aed1; _gid=GA1.2.744610889.1564918547; _sp_ses.1a3e=*; _pk_id.421.1a3e=d0719d65cdc23658.1561868168.36.1564918549.1564765819.; _sp_id.1a3e=89c8d259-3644-4e22-9add-b59197aef96c.1561868166.69.1564918550.1564901698.2cca91f7-11fb-4ebc-8156-bb9a0397d78e; stockx_bid_ask_spread_seen=true",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
        "Referer": "https://stockx.com/buying",
        "JWT-Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA4LTAyIDE3OjA1OjQ1IiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic25lYWtlcnMiLCJpc19hZG1pbiI6IjAiLCJzZXNzaW9uX2lkIjoiMTMxMjIyMTU1MzE0Mzc2MjI2MzEiLCJleHAiOjE1NjUzNzAzNDUsImFwaV9rZXlzIjpbXX0.af-2Iu0Qj12s-sZ9K1L824lV4vtLqveDcoTZGkdMycE",
    }

requests.packages.urllib3.disable_warnings()
session = requests.session()

def conn_db():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='12345678',
        db='shoes',
        charset='utf8'
    )
    cur = conn.cursor()
    return conn,cur

def conn_close(conn,cur):
    cur.close()
    conn.close()

def conn_commit(cur):
    cur.connection.commit()

def go():
    for i in range(1, 18):
        history_url = "https://stockx.com/api/customers/5350379/buying/history?sort=matched_with_date&order=DESC&limit=20&page="+str(i)+"&currency=USD"
        his_json = json.loads(session.get(url=history_url, headers=headers,verify=False).text)

        for i in range(len(his_json['PortfolioItems'])):
            content_dict = his_json['PortfolioItems'][i]

            time_1 = content_dict['matchedWithDate'].replace("+00:00", ".000Z")
            data_1 = datetime.strptime(time_1, '%Y-%m-%dT%H:%M:%S.%fZ')
            purchase_time = data_1 + timedelta(hours=8)
            purchase_time = purchase_time.strftime("%Y-%m-%d")

            orderNumber = content_dict['orderNumber'].strip()
            shoesName = content_dict['product']['title'].strip()
            styleId = content_dict['product']['styleId'].strip()
            shoeSize = content_dict['product']['shoeSize']
            amount = content_dict['localTotal']
            purchaseDate = purchase_time
            trackingNo = content_dict['Tracking']['number'].strip()

            print(
                orderNumber,"\t",
                shoesName,"\t",
                styleId,"\t",
                shoeSize,"\t",
                amount,"\t",
                purchaseDate,"\t",
                trackingNo)

            sql = "insert into stockx_purchased(orderNumber,shoesName,styleId,shoeSize,amount,purchaseDate,trackingNo) VALUES ('%s','%s','%s','%s','%s','%s','%s')" %(orderNumber,shoesName,styleId,shoeSize,amount,purchaseDate,trackingNo)
            cur.execute(sql)


conn,cur = conn_db()
go()
conn_commit(cur)
conn_close(conn, cur)
