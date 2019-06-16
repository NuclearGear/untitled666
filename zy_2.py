import requests
import time
import json
from lxml import etree

def toStrStrip(param):
    return str(param).strip()

def getHtml(url):

    pass


def product_name(html_selector):
    for i in html_selector.xpath("//dl[@class='detail']/dd/table/tr"):
        if i.attrib != "":
            return i.xpath(".//span/text()")[0]


def table_detail(order_item_names):
    tr_list = order_item_names.xpath("//tr/@class")
    # print(type(tr_list))
    if tr_list != None:
        for i in range(len(tr_list)):
            print(tr_list[i])

for i in range(1,29):
    all_url = "http://member.transrush.com/Ajax/AjaxTransportInfo.aspx?actionType=1&pidx="+str(i)+"&psize=10&day=180&pid=&wid=&orderno=&tuid=970346&time=1559310888853"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
        "Cookie": "_ga=GA1.2.1118471410.1543457100; UM_distinctid=16771cc94a483-0ad443cb105f17-546f3a7b-1aeaa0-16771cc94a57d6; acw_tc=2a51041915580589923975605e818ad3542b4e01e31939013be7f6ba6a; ASP.NET_SessionId=n5qskp45orgdio55kexqqxmt; SESSION_COOKIE=10.104.2.215; Hm_lvt_5f97b18de3423180375703d5f0196b0c=1557975907,1558058912,1558062657,1558321472; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1558321472; _gid=GA1.2.742223138.1558321472; Qs_lvt_271648=1557975907%2C1557976000%2C1557976005%2C1558058912%2C1558321472; Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1557976005,1558058912,1558062657,1558321472; User::UserID=Y243F3i2u034Q3k0C0z1q1Z2M0u060L0; User::UserCode=r3H0I2Y3B281J02021i0p360m1A1T0C0; User::EMail=r0C3h252U1z2M3L212u3h2f2o362V1K0q3M303e2y2o004C0a0C0B1n1a3A1r3V2; User::TUserID=970346; User::TrueName=%e5%ad%99%e9%9b%b7; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; User::Mobile=33e1F0o2Y3n3v1C1H0b150d033R364e3; TransrushUserInfo=vnU1l7WyoC25oJCcZekcLJHWYB3gCy1M9zxpA1E1l5MCHvp+Vt9CBIupJyf/r/3AbxGGVdPzeMLHdgjJgLSZRKfhV5hW7GZYJ4xlCrziaIJSlG/1EibfGfe/HG6GfaJwcA2O2EQC/y9FIUo8ksGS1KWOkuvwMBXVtmGh+hl+iBdO6220ZQJQmVmJAAXoWRwrRNzZob3kMw47ZB1UPFACBmxB5/ympDxI; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1557976001,1557976005,1558062661,1558321478; _gat=1; SiteCode=CN; SiteName=j1m183L1H00160N110Q2Z1z1L0n2I0T2; Marketing=g1m0i1h2r2F1e1v1v1j133t1i191W1Z124Z3T1y280i3q3G2c114U382d020f3t2; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1558321893; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1558321893; Qs_pv_271648=866960178601255000%2C4051141332852205600%2C1521252403792763400%2C4286530082006524000%2C4026643335475952000",
        "Referer": "http://member.transrush.com/Member/MyParcel.aspx"
    }
    session = requests.session()

    all_text_dict = json.loads(session.get(url=all_url,headers=headers).text)

    for i in range(0,len(all_text_dict['ResultList'])):
        zy_orderCreateTime = all_text_dict['ResultList'][i]['CreateTime']
        if all_text_dict['ResultList'][i]['OrderNo'].startswith('DD'):
            order_detail_url = "http://member.transrush.com/Member/parcelDetail.aspx?fromTab=sy&orderNo="+all_text_dict['ResultList'][i]['OrderNo']
            # order_detail_url = "http://member.transrush.com/Member/parcelDetail.aspx?fromTab=dqs&orderNo=DD190214608236"
            order_detail_html = session.get(url=order_detail_url, headers=headers).text
            html_selector = etree.HTML(order_detail_html)

            product_count = html_selector.xpath("//dl[@class='detail']/dd/table/tr")

            orderID = all_text_dict['ResultList'][i]['OrderNo']
            order_status = html_selector.xpath("//*[@id='detail']/ul/li[1]/span[2]/strong/text()")[0]
            order_address = html_selector.xpath("//dl[@class='address']/dd/ul/li[2]/span[@class='cont']/text()")[0]
            order_transfer_depot = html_selector.xpath("//ul[@class='clearfix']/li[2]/span[2]/text()")[0]
            order_tracking = html_selector.xpath("//ul[@class='clearfix']/li[3]/span[2]/text()")[0]
            order_domestic = html_selector.xpath("//ul[@class='clearfix']/li[4]/span[2]/text()")[0]
            order_service_lines = html_selector.xpath("//ul[@class='clearfix']/li[5]/span[2]/text()")[0]
            order_post_time = html_selector.xpath("//ul[@class='clearfix']/li[6]/span[2]/text()")[0]
            order_total_cost = html_selector.xpath("//*[@id='detail']/dl[5]/dd/ul/li[4]/span[2]/text()")[0]

            for i in html_selector.xpath("//dl[@class='detail']/dd/table/tr"):
                if i.attrib != "":
                    # 判断tr/td[1] rowspan属性
                    if len(i.xpath("./td[1][@rowspan]")):
                        # print(i.xpath("./td[1]/@title"Ωn)[0],i.xpath(".//span/text()")[0])
                        rowspan = i.xpath("./td[1]/@rowspan")[0]
                        if int(rowspan) > 1:
                            print(
                                zy_orderCreateTime, "\t",# 2019-05-30
                                toStrStrip(str(i.xpath('./td[3]/@title')[0])),"\t",#SZ13 homage 1 eb 5.7
                                toStrStrip(order_tracking), "\t",#94055096999375084386gitgggggg94
                                toStrStrip(order_status), "\t",#待出库
                                toStrStrip(order_domestic), "\t",# 9737401138397(青岛邮政包裹)
                                toStrStrip(orderID),"\t",#DD190528281703
                                toStrStrip(order_total_cost),"\t",#￥134.00
                                order_address[order_address.find("市")+1:order_address.find("市")+4],"\t",#东城区
                                toStrStrip(order_transfer_depot),"\t",#美国波特兰（免税仓）
                                toStrStrip(order_service_lines),"\t",#关税补贴模式-鞋服关税补贴专线
                                toStrStrip(order_post_time).split(" ")[0]
                            )
                            # 获取第三个a标签后面的第N个标签："//a[@id='3']/following-sibling::*[N]"
                            for j in range(2, int(rowspan) + 1):
                                xpath_express = "./following-sibling::tr[" + str(j - 1) + "]"
                                row_conten = i.xpath(xpath_express)
                                for k in row_conten:
                                    # print(etree.tostring(k))
                                    print(
                                        zy_orderCreateTime,"\t",# 2019-05-30
                                        toStrStrip(str(k.xpath('./td[2]/@title')[0])),"\t",# SZ13 homage 1 eb 5.7
                                        toStrStrip(order_tracking),"\t",# 94055096999375084386gitgggggg94
                                        toStrStrip(order_status),"\t",# 待出库
                                        toStrStrip(order_domestic),"\t",# 9737401138397(青岛邮政包裹)
                                        toStrStrip(orderID),"\t",# DD190528281703
                                        toStrStrip(order_total_cost),"\t",# ￥134.00
                                        order_address[order_address.find("市") + 1:order_address.find("市") + 4],"\t",# 东城区
                                        toStrStrip(order_transfer_depot),"\t",# 美国波特兰（免税仓）
                                        toStrStrip(order_service_lines),"\t",# 关税补贴模式-鞋服关税补贴专线
                                        toStrStrip(order_post_time).split(" ")[0]
                                    )
                        else:
                            print(
                                zy_orderCreateTime,"\t",# 2019-05-30
                                toStrStrip(str(i.xpath('./td[3]/@title')[0])),"\t",# SZ13 homage 1 eb 5.7
                                toStrStrip(str(i.xpath('./td[1]/@title')[0])),"\t",# 94055096999375084386gitgggggg94
                                toStrStrip(order_status),"\t",# 待出库
                                toStrStrip(order_domestic),"\t",# 9737401138397(青岛邮政包裹)
                                toStrStrip(orderID),"\t",# DD190528281703
                                toStrStrip(order_total_cost),"\t",# ￥134.00
                                order_address[order_address.find("市") + 1:order_address.find("市") + 4],"\t",# 东城区
                                toStrStrip(order_transfer_depot),"\t",# 美国波特兰（免税仓）
                                toStrStrip(order_service_lines),"\t",# 关税补贴模式-鞋服关税补贴专线
                                toStrStrip(order_post_time).split(" ")[0]
                            )
        else:
            print("","\t","","\t",all_text_dict['ResultList'][i]['OrderNo'])



