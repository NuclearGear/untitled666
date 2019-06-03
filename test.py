from datetime import datetime,timedelta
import time
import requests
from lxml import etree

# date_ = datetime.strptime('2018-08-06T10:00:00.000Z',"%Y-%m-%dT%H:%M:%S.%fZ")
# #local_time = 2018-08-06 18:00:00
# local_time = date_ + timedelta(hours=8)
# print(local_time)

# time = 1558656143074
# time_detail = round(time.time()*1000)
# print(time_detail)
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
        "Cookie": "_ga=GA1.2.1118471410.1543457100; UM_distinctid=16771cc94a483-0ad443cb105f17-546f3a7b-1aeaa0-16771cc94a57d6; acw_tc=2a51041915580589923975605e818ad3542b4e01e31939013be7f6ba6a; ASP.NET_SessionId=n5qskp45orgdio55kexqqxmt; SESSION_COOKIE=10.104.2.215; Hm_lvt_5f97b18de3423180375703d5f0196b0c=1557975907,1558058912,1558062657,1558321472; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1558321472; _gid=GA1.2.742223138.1558321472; Qs_lvt_271648=1557975907%2C1557976000%2C1557976005%2C1558058912%2C1558321472; Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1557976005,1558058912,1558062657,1558321472; User::UserID=Y243F3i2u034Q3k0C0z1q1Z2M0u060L0; User::UserCode=r3H0I2Y3B281J02021i0p360m1A1T0C0; User::EMail=r0C3h252U1z2M3L212u3h2f2o362V1K0q3M303e2y2o004C0a0C0B1n1a3A1r3V2; User::TUserID=970346; User::TrueName=%e5%ad%99%e9%9b%b7; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; User::Mobile=33e1F0o2Y3n3v1C1H0b150d033R364e3; TransrushUserInfo=vnU1l7WyoC25oJCcZekcLJHWYB3gCy1M9zxpA1E1l5MCHvp+Vt9CBIupJyf/r/3AbxGGVdPzeMLHdgjJgLSZRKfhV5hW7GZYJ4xlCrziaIJSlG/1EibfGfe/HG6GfaJwcA2O2EQC/y9FIUo8ksGS1KWOkuvwMBXVtmGh+hl+iBdO6220ZQJQmVmJAAXoWRwrRNzZob3kMw47ZB1UPFACBmxB5/ympDxI; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1557976001,1557976005,1558062661,1558321478; _gat=1; SiteCode=CN; SiteName=j1m183L1H00160N110Q2Z1z1L0n2I0T2; Marketing=g1m0i1h2r2F1e1v1v1j133t1i191W1Z124Z3T1y280i3q3G2c114U382d020f3t2; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1558321893; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1558321893; Qs_pv_271648=866960178601255000%2C4051141332852205600%2C1521252403792763400%2C4286530082006524000%2C4026643335475952000",
        "Referer": "http://member.transrush.com/Member/MyParcel.aspx"
    }
res = requests.get(url="http://member.transrush.com/Member/parcelDetail.aspx?fromTab=sy&orderNo=DD190214608236",headers=headers).text

detail_html = etree.HTML(res)
detail_dl = detail_html.xpath("//dl[@class='detail']/dd/table/tr")

for i in detail_html.xpath("//dl[@class='detail']/dd/table/tr"):
    # if detail_dl[i].attrib != "":
    #     detail_dl[i].xpath("//td/@title")
        for j in detail_dl[i].xpath("//td/@title"):
            print(i,j)






