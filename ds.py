# -*- coding: gbk -*-

###############################################################################
#use data from baidumap and darksky.net for weather forecast ,umicore's module#
#                     author:batt1ebear                                       #
###############################################################################
import urllib
import urllib2
import json
import time

def getloca(loca):
    url='http://api.map.baidu.com/geocoder/v2/?address='+loca+\
    '&output=json&ak=GrfpdE3WyT8ZY6oOnb26pCxPEBLxGkuO&callback=showLocation'
    rawdata=urllib2.urlopen(url)
    readit=rawdata.read()
    r=readit[27:-1]
    reloca=json.loads(r)
    return reloca['result']['location']['lat'],reloca['result']['location']['lng']
    
def ds_daily(loca):
    lat,lng=getloca(loca)
    url='https://api.darksky.net/forecast/'+'55a4d919a5ea39183daac7d8bb7d3012/'+str(lat)+','+str(lng)\
        +'?exclude=currently,minutely,hourly?units=si'
    rawdata=urllib2.urlopen(url)
    readit=rawdata.read()
    data=json.loads(readit)
    response=u"最高气温：{:.2f} 最低气温：{:.2f}\n最高体感温度：{:.2f}\nuv指数：{}\n湿度：{}\n可见度：{}\n降水几率：{}\n日落时间：{}\n月相：{}"\
        .format((data['daily']['data'][0]['temperatureHigh']-32)/1.8,(data['daily']['data'][0]['temperatureLow']-32)/1.8,(data['daily']['data'][0]['apparentTemperatureHigh']-32)/1.8,\
        data['daily']['data'][0]['uvIndex'],data['daily']['data'][0]['humidity'],data['daily']['data'][0]['visibility'],data['daily']['data'][0]['precipProbability'],data['daily']['data'][0]['sunsetTime'],data['daily']['data'][0]['moonPhase'])
    return response

def ds_cloud(loca):
    lat,lng=getloca(loca)
    url='https://api.darksky.net/forecast/'+'55a4d919a5ea39183daac7d8bb7d3012/'+str(lat)+','+str(lng)\
        +'?exclude=currently,minutely,daily?units=si'
    rawdata=urllib2.urlopen(url)
    readit=rawdata.read()
    data=json.loads(readit)
    response=u'12小时云量预报\n时间 云覆盖率 降水几率'
    
    for h in range(0,11):
        text='\n{}   {}     {}'.format(time.strftime("%H:%M", time.gmtime(data['hourly']['data'][h]['time']+28800)),data['hourly']['data'][h]['cloudCover'],data['hourly']['data'][h]['precipProbability'])
        response=response+text
        
    return response

#thedata=ds_daily('南京信息工程大学')
thedata=ds_cloud('南京信息工程大学')
str=thedata.encode('gbk')
print str

