import time
import json
import requests

now = str(time.time() * 1000)
newnow = now.split('.')[0]

email = '645748712@qq.com'
pwd = 'sl5862798'

ref = 'http://member.transrush.com/Member/MyParcel.aspx'

last = str(time.time() * 1000 - 901234)

form_data = {
    'time': newnow,
    'actionType': '0',
    'pwd': pwd,
    'email': email,
    'isRememberPwd': 'true',
    'ref': ref,
    '_': last
}

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
    "Cookie": "_ga=GA1.2.1118471410.1543457100; UM_distinctid=16771cc94a483-0ad443cb105f17-546f3a7b-1aeaa0-16771cc94a57d6; acw_tc=2a51041915580589923975605e818ad3542b4e01e31939013be7f6ba6a; ASP.NET_SessionId=n5qskp45orgdio55kexqqxmt; SESSION_COOKIE=10.104.2.215; Hm_lvt_5f97b18de3423180375703d5f0196b0c=1557975907,1558058912,1558062657,1558321472; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1558321472; _gid=GA1.2.742223138.1558321472; Qs_lvt_271648=1557975907%2C1557976000%2C1557976005%2C1558058912%2C1558321472; Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1557976005,1558058912,1558062657,1558321472; User::UserID=Y243F3i2u034Q3k0C0z1q1Z2M0u060L0; User::UserCode=r3H0I2Y3B281J02021i0p360m1A1T0C0; User::EMail=r0C3h252U1z2M3L212u3h2f2o362V1K0q3M303e2y2o004C0a0C0B1n1a3A1r3V2; User::TUserID=970346; User::TrueName=%e5%ad%99%e9%9b%b7; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; User::Mobile=33e1F0o2Y3n3v1C1H0b150d033R364e3; TransrushUserInfo=vnU1l7WyoC25oJCcZekcLJHWYB3gCy1M9zxpA1E1l5MCHvp+Vt9CBIupJyf/r/3AbxGGVdPzeMLHdgjJgLSZRKfhV5hW7GZYJ4xlCrziaIJSlG/1EibfGfe/HG6GfaJwcA2O2EQC/y9FIUo8ksGS1KWOkuvwMBXVtmGh+hl+iBdO6220ZQJQmVmJAAXoWRwrRNzZob3kMw47ZB1UPFACBmxB5/ympDxI; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1557976001,1557976005,1558062661,1558321478; _gat=1; SiteCode=CN; SiteName=j1m183L1H00160N110Q2Z1z1L0n2I0T2; Marketing=g1m0i1h2r2F1e1v1v1j133t1i191W1Z124Z3T1y280i3q3G2c114U382d020f3t2; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1558321893; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1558321893; Qs_pv_271648=866960178601255000%2C4051141332852205600%2C1521252403792763400%2C4286530082006524000%2C4026643335475952000",
    "Referer": "http://member.transrush.com/Member/MyParcel.aspx"
}

login_url = "http://passport.transrush.com/AjaxPassport.aspx?" \
            "time=1558322336473&actionType=0&pwd=sl5862798&email=645748712%40qq.com&isRememberPwd=false&ref=&_=1558322325354"

session = requests.session()
response = session.get(url=login_url, params=form_data, headers=headers)

print(response.text)

for i in range(1, 26):
    # 所有包裹url 6个月
    tracking_url = "http://member.transrush.com/Ajax/AjaxTransportInfo.aspx?" \
                   "actionType=1&pidx=" + str(i) + "&psize=10&day=2019&pid=&wid=&orderno=&tuid=970346&time=1558406194326"

    track_res = session.get(url=tracking_url, headers=headers)
    full_dict = json.loads(track_res.text)

    totalCount = full_dict['TotalCount']
    totalPage = full_dict['TotalPage']
    pageSize = full_dict['PageSize']

    detail_list = full_dict['ResultList']
    for i in range(len(detail_list)):
        det_OrderNo = detail_list[i]['OrderNo']
        det_CreateTime = detail_list[i]['CreateTime']
        det_OrderState = detail_list[i]['OrderState']
        det_trans_mode = detail_list[i]['ProductName']
        det_trans_address = detail_list[i]['VWarehouseName']
        det_trans_seller_track = detail_list[i]['DeliveryCode']
        det_trans_OrderTypeFlag = detail_list[i]['OrderTypeFlag']

        time_detail = round(time.time()*1000)
        # 物流订单具体内容
        # http: // member.transrush.com / ajax / AjaxTransportInfo.aspx?
        # actionType = 6 & orderno = DD181218136618 & ordertypeflag = 3 & time = 1558656143074
        one_trans_info_url = "http://member.transrush.com/ajax/AjaxTransportInfo.aspx?actionType=6&orderno="+det_OrderNo+"&ordertypeflag="+str(det_trans_OrderTypeFlag)+"&time="+str(time_detail)
        one_trans_info_url_response = session.get(url=one_trans_info_url,headers=headers)
        # print(track_content_response.text)
        one_trans_info_dict = json.loads(one_trans_info_url_response.text)

        if(one_trans_info_dict['ProductList'] != None):
            for i in range(len(one_trans_info_dict['ProductList'])):
                one_trans_info_ProductName = one_trans_info_dict['ProductList'][i]['ProductName']

                taxCost = float(one_trans_info_dict['TariffPrice'])
                one_trans_info_TotalCosts = float(one_trans_info_dict['TotalCosts']) + taxCost

                one_trans_info_OrderTypeFlag = one_trans_info_dict['OrderTypeFlag']
                one_trans_info_StatusFlag = one_trans_info_dict['StatusFlag']
                one_trans_info_OrderState = one_trans_info_dict['OrderState']
                one_trans_info_PayFlag = one_trans_info_dict['PayFlag']
                one_trans_info_AddressID = one_trans_info_dict['OrderAddress']['AddressID']
                # 转运 入出库信息
                # for i in range(len(one_trans_info_dict['TransportLogistics'])):
                #     TransportLogistics_dict = one_trans_info_dict['TransportLogistics'][i]
                    # print(TransportLogistics_dict['HappenTime']+"---"+TransportLogistics_dict['StateName'])

                # http: // member.transrush.com / ajax / ajaxUser.aspx?actionType = 6 & takeUserId = 0 & addressId = 0 & ordertypeflag = 3 & payflag = 2 & statusflag = 2 & orderno = DD190523121885 & time = 1558694023141
                one_trans_info_address_url = "http://member.transrush.com/ajax/ajaxUser.aspx?actionType=6&takeUserId=0&addressId="+ str(one_trans_info_AddressID) +"&ordertypeflag="+ str(one_trans_info_OrderTypeFlag) +"&payflag="+ str(one_trans_info_PayFlag) +"&statusflag="+ str(one_trans_info_StatusFlag) +"&orderno="+ det_OrderNo +"&time="+str(round(time.time()*1000))
                one_trans_info_address_dict = json.loads(session.get(url=one_trans_info_address_url,headers=headers).text)
                one_trans_info_address = one_trans_info_address_dict['AreaNamePath']

                print(
                    det_CreateTime,"\t",
                    one_trans_info_ProductName,"\t",
                    det_OrderNo,"\t",
                    one_trans_info_TotalCosts,"\t",
                    det_trans_seller_track,"\t",
                    det_OrderState,"\t",
                    det_trans_mode,"\t",
                    one_trans_info_address,"\t",
                    det_trans_address
                )
        else:
            one_trans_info_OrderTypeFlag = one_trans_info_dict['OrderTypeFlag']
            unclaimed_url = "http://member.transrush.com/ajax/AjaxTransportInfo.aspx?actionType=6&orderno="+det_OrderNo+"&ordertypeflag="+str(one_trans_info_OrderTypeFlag)+"&time"+str(round(time.time()*1000))
            unclaimed_dict = json.loads(session.get(url=unclaimed_url,headers=headers).text)
            print(
                unclaimed_dict['TransportLogistics'][0]['HappenTime'],"\t",
                "","\t",
                "","\t",
                "","\t",
                det_OrderNo,"\t",
                unclaimed_dict['OrderState'],"\t"
            )