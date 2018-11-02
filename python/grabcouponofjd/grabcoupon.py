#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests

# 根据京东活动页面的接口编写定时抢劵脚本
# 实际抓到的接口：https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22xGyRxi5wSZ2qtmSUoxiS1thbqpy%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3D3457b7f1a1574b9fbe75c2ca79ad0092%2CroleId%3D15241749%22%2C%22eid%22%3A%22LQKUBLBZYQELZ6FKWKTEREUNPL7JKQVTVCPCZS4JTALVVA3HCEAXV7NZUZ7FU2TUPLTT44IYVOE2GQS6KAQ32XQWIQ%22%2C%22fp%22%3A%22d9e2787693141e277acaf1d7d40dc826%22%2C%22pageClick%22%3A%22Babel_Coupon%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22%22%2C%22lat%22%3A%22%22%7D%7D&screen=750*1334&client=wh5&clientVersion=1.0.0&sid=&uuid=&area=&loginType=3&callback=jsonp3
# Request Method: GET


# 请求优惠价接口
def grabcouponjson():
    # Request Header取header数据
    header = {
        'Host': 'https://pro.jd.com',
        'Referer': 'https://pro.jd.com/mall/active/xGyRxi5wSZ2qtmSUoxiS1thbqpy/index.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'cookie':'shshshfpb=20895782221094c93af5cc10eec0f669c5ab020ee38685e9073b5bce83; shshshfpa=ef6018a4-ecd4-e9e8-de4f-b44539aafeb4-1540983388; __jdc=122270672; __jdu=1540983388020707374683; PCSYCityID=1213; TrackID=1ITJrScUoBQBbiz5ER5Lf92atS4Wox4R_svgLrUW2u5W41VhiCUs83psKWuVWGnEjVvATPqkVrdW2adbEORGDfIym1ibRPqVFWcf9EyQLGFn4XUMy3Rui6-XHEmuQ_1qn; pinId=aQ9km7ASYmKUpKyWAWQ6Lw; pin=xzy1193487537; unick=xzy1193487537; ceshi3.com=201; _tp=Qgu80Gn9T7%2BnCO9B8a9gpA%3D%3D; _pst=xzy1193487537; user-key=c981744e-78d6-40c3-909a-46af948102f7; ipLoc-djd=1-72-2799-0; mt_xid=V2_52007VwMWV1xQW1gdQBBdBmYFE1RfXlddFkspDg01VEFRW1tOU0gaGEAAZQUQTg5aU1IDSEpYDWVTFwUIXVJeL0oYXAx7AxJOXFtDWx1CGVoOYwMiUG1YYlkdShBcA2EFFmJdXVRd; cn=51; __jda=122270672.1540983388020707374683.1540983388.1541124021.1541127830.4; unpl=V2_ZzNtbUJWEEB0WhVVcx9bBWIFFFkSVhEQfAwWB31KWVcyUEcOclRCFXwURlRnGF8UZwMZX0FcQBBFCHZUehhdBGYBFV5GZxpFKwhFVidSbDVkAyJVcldHEHQAT1Z5EFUEZAIUXERVRRByAURkSx5sNVcCIlxyVnNeGwkLVH8cXQ1uARBUS1ZAFHMJQFZ9HFsMZTMTbUE%3d; __jdv=122270672|www.hao123.com|t_1000003625_hao123mz|tuiguang|10bd0cb097614775a0c485ab7b4cdbdb|1541129546564; thor=F1A6F9029830C144DE4E6A3CE19A73E12CE55393D2AC0DFB13756D9029F97A3608B73E226CB9D67650F2C217C7E2CD445FFF5F9D42FEEF6004DAF0EF52BBD89524ED72D159026E15A5D7876F3285571C5DD78838E1E07C7263D2066250C3D24290531F47135FF0D3B750A48DD1BF3A4687157D2A7BC86B9E3F4A6A95FDFE182DD571B1524F8519977A16EA5F412258EF; shshshfp=16f9c14e76c8dfe916a56acf71494cac; shshshsID=c4a1c5d8e9f18f82a91a3aa1a738f37f_3_1541129559889; 3AB9D23F7A4B3C9B=LQKUBLBZYQELZ6FKWKTEREUNPL7JKQVTVCPCZS4JTALVVA3HCEAXV7NZUZ7FU2TUPLTT44IYVOE2GQS6KAQ32XQWIQ; __jdb=122270672.4.1540983388020707374683|4.1541127830',
    }

    url ='https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22xGyRxi5wSZ2qtmSUoxiS1thbqpy%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3D3457b7f1a1574b9fbe75c2ca79ad0092%2CroleId%3D15241749%22%2C%22eid%22%3A%22LQKUBLBZYQELZ6FKWKTEREUNPL7JKQVTVCPCZS4JTALVVA3HCEAXV7NZUZ7FU2TUPLTT44IYVOE2GQS6KAQ32XQWIQ%22%2C%22fp%22%3A%22d9e2787693141e277acaf1d7d40dc826%22%2C%22pageClick%22%3A%22Babel_Coupon%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22%22%2C%22lat%22%3A%22%22%7D%7D&screen=750*1334&client=wh5&clientVersion=1.0.0&sid=&uuid=&area=&loginType=3&callback=jsonp2'

    response = requests.get(url, headers=header)
    # response = requests.get(url, headers=header, allow_redirects=False)

    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.json()
    return response


if __name__ == '__main__':
    result = grabcouponjson()
    print("result:{}", result)


