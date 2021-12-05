#todo
#根据用户输入返回查询结果
#如果必要信息不足需要引导用户继续输入
import requests
from bs4 import BeautifulSoup
from wechatpy import parse_message, create_reply
from django.http import HttpResponse

def crawlweather():  # 爬取天气数据
    url = 'http://www.weather.com.cn/weather/101010100.shtml'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

    resp = requests.get(url, headers)
    resp.encoding = 'utf-8'
    date = []
    weather = []
    temp_h = []
    temp_l = []
    wind = []
    windlevel = []
    bs = BeautifulSoup(resp.text, 'lxml')
    datelab = bs.select('ul.clearfix>li.sky>h1')
    for each in datelab:
        date.append(each.text)
    wealab = bs.select('ul.clearfix>li.sky>p.wea')
    for each in wealab:
        weather.append(each.text)
    tem_high_lab = bs.select('ul.clearfix>li.sky>p.tem>span')
    for each in tem_high_lab:
        temp_h.append(each.text)
    tem_low_lab = bs.select('ul.clearfix>li.sky>p.tem>i')
    for each in tem_low_lab:
        temp_l.append(each.text)
    winlab = bs.select('ul.clearfix>li.sky>p.win>em>span')
    for each in winlab:
        wind.append(each.get('title'))
    windlevlab = bs.select('ul.clearfix>li.sky>p.win>i')
    for each in windlevlab:
        windlevel.append(each.text)
    return date, weather, temp_h, temp_l, wind, windlevel  # 返回存储数据的五个数组

def queryweather(num, msg):
    daycount=0
    if num == "三" or num == "3":
        daycount = 3
    elif num == "七" or num == "7":
        daycount = 7
    else:
        daycount=1
    date, weather, temp_h, temp_l, wind, windlevel = crawlweather()
    res = ""
    for i in range(0, daycount):
        res = res + date[i] + '  '+ weather[i] + '  '+ temp_h[i] + "/" + temp_l[i] + '  '+wind[i] + windlevel[i]+'\n'
    print(res)
    reply = create_reply(res, msg)
    return reply


def Query(msg):
    if msg.content =='查询天气':
        return queryweather("7", msg)
    else:
        return create_reply("123", msg)

queryweather("7",1)