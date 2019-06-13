import requests
import json
requests.packages.urllib3.disable_warnings()

headers = {
    "cookie":"CNZZDATA1272882183=695475915-1547168187-%7C1559822032; FSSBBIl1UgzbN7N80T=3PMHeuGTYJDDtcAeAVHuxXQkdVNzZbnm66v2dy5l62UsQhdJbyAOIt3HP33o5i.vpqhEf5_2mM6wHJgqluykIL9ZkImIiispzWhbY.89haS_D5Aqi4kwk0YsMn_RM0X75Gg5ivwjdxLxz6.Z2bd6fKipx2DVxh0fhFCb2qtS0rX3oP5XY5kn47RLkqRYRiQQZBmZeRexr0zcEnekRWOxUjEPCO.3yDpYWyVwUwiou0p7X7atmp7QnNDCyk3OG5yiy8GTE60YVwhRvF4JMt1cqK5YLDY6XRb5WPBf5vqNx.lVpEP_GeDZk0eUhD8Ziaczh4lVKYYoSFIxy0ZEd1Qea.Daq; FSSBBIl1UgzbN7N80S=Ylcluc2O9GYcU2wjVuHsjjBRXax0W8EL.nCyDEmcib.Bdgswb3yvJ7ZJfxc0AUOy; UM_distinctid=1683a75a3ef79-0c2ee0f94e68078-1b79162d-4a574-1683a75a3f03f9",
    "user-agent":"duapp/4.1.1 (com.siwuai.duapp; build:4.1.1; iOS 12.3.1) Alamofire/4.8.2",
    # "",
    # "",
    # "",
    # "",
    # "",
    # ""
}
formdata = {
    "accessToken":"",
    "code":"",
    "countryCode":"86",
    "expire":"0",
    "mode":"0",
    "openId":"",
    "password":"53a790fe93781efd3158c96df48ce2b9",
    "platform":"iPhone",
    "refreshToken":"",
    "sign":"62f9da007d338d2f690764b9c070f423",
    "sourcePage":"",
    "timestamp":"1559831124753",
    "token":"JLIjsdLjfsdII%3D%7CMTQxODg3MDczNA%3D%3D%7C07aaal32795abdeff41cc9633329932195",
    "type":"pwd",
    "userName":"15901312329",
    "uuid":"B439DA6B-3DAE-4882-A982-357AEC7003F1",
}


# https://m.poizon.com/client/setPushToken?newSign=f01b214e97bec5e4e61e5c0b5a5cb00b
search_product_url = "https://m.poizon.com/users/unionLogin?newSign=92e018e7936aec3a10f3058f75e56b3a"

# session = requests.session()
response = requests.post(url=search_product_url,data=formdata,headers=headers,verify=False)
print(response.status_code)

# for i in json.loads(response.text)['data']:
#     print(i)
