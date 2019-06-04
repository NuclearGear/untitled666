import requests
from lxml import etree
import json

feedback_url = "http://member.transrush.com/ajax/AjaxUserInfo.aspx?time=1559662299508&actionType=7&pidx=1&psize=20&feedbackno=&message=&starttime=&endtime="
waiting_url = "http://member.transrush.com/Ajax/AjaxTransportInfo.aspx?actionType=16&pidx=1&psize=30&day=180&pid=&wid=&orderno=&tuid=970346&time=1559662480988"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
    "Cookie": "mediav=%7B%22eid%22%3A%22565776%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%223b9CVu%3CeRI%3AVc%40%5BLq5Dn%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.1512425580.1543337347; ASP.NET_SessionId=mrmco4e4fn3kawrrak33mo55; SESSION_COOKIE=10.104.2.215; _gid=GA1.2.1091921248.1559020581; Hm_lvt_5f97b18de3423180375703d5f0196b0c=1556856122,1559020581; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; User::Mobile=33e1F0o2Y3n3v1C1H0b150d033R364e3; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1557135238,1559020585; SiteCode=CN; SiteName=j1m183L1H00160N110Q2Z1z1L0n2I0T2; Marketing=g1m0i1h2r2F1e1v1v1j133t1i191W1Z124Z3T1y280i3q3G2c114U382d020f3t2; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1559274046; UM_distinctid=16b0bf9c48b51d-0f5ed883efec28-37647e03-384000-16b0bf9c48c117; User::UserID=Y243F3i2u034Q3k0C0z1q1Z2M0u060L0; User::UserCode=r3H0I2Y3B281J02021i0p360m1A1T0C0; User::EMail=r0C3h252U1z2M3L212u3h2f2o362V1K0q3M303e2y2o004C0a0C0B1n1a3A1r3V2; User::TUserID=970346; User::TrueName=%e5%ad%99%e9%9b%b7; TransrushUserInfo=vnU1l7WyoC25oJCcZekcLJHWYB3gCy1M9zxpA1E1l5MCHvp+Vt9CBIupJyf/r/3AbxGGVdPzeMLHdgjJgLSZRKfhV5hW7GZYJ4xlCrziaIJSlG/1EibfGfe/HG6GfaJwcA2O2EQC/y9FIUo8ksGS1KWOkuvwMBXVtmGh+hl+iBdO6220ZQJQmVmJAAXoWRwrRNzZob3kMw47ZB1UPFACBmxB5/ympDxI; Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1559020581; Qs_lvt_271648=1559383406%2C1559454626%2C1559561543%2C1559608322%2C1559656101; EbayVCode=D0JR; acw_tc=2a51041b15596612993764493e37537f04650baa3c293e452a767d3f8b; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1559661300; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1559661300; Qs_pv_271648=3273747839559311400%2C539533334058263200%2C546464348266373950%2C4026505967389504500%2C1845041700948029700"
    # "Referer": "http://member.transrush.com/Member/MyParcel.aspx"
}
session = requests.session()
response = session.get(url=waiting_url,headers=headers)

undone_orderNo_list = []
def undone_gongdan(feedback_url):
    for j in json.loads(session.get(url=feedback_url, headers=headers).text)['ResultList']:
        if j['ProcessState'] != "已完结":
            undone_orderNo_url = "http://member.transrush.com/Member/MyFeedbackDetail.aspx?Id="+str(j['Id'])
            undone_orderNo = etree.HTML(session.get(url=undone_orderNo_url,headers=headers).text).xpath("//b[@id='bOrderCode']/text()")[0]
            undone_orderNo_list.append(undone_orderNo)
    return undone_orderNo_list

print(undone_gongdan(feedback_url))
for i in json.loads(response.text)['ResultList']:
    if i['OrderNo'] not in undone_gongdan(feedback_url):
        print(i['OrderNo'])
