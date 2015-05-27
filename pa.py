#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'brucezheng'
#对学校的就业信息网，招聘会信息进行采集
import urllib
import urllib2
import re

#page = 1
#url = 'http://www.qiushibaike.com/hot/page/' + str(page)
url = 'http://jy.seu.edu.cn/detach.portal?.pen=pe781&.pmn=view&action=queryAllZphManageView'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
  #  pattern = re.compile('<a.*?style="cursor: pointer".*?onclick="queryMoreDwList.*?>(.*?)</a>',re.S)
    pattern = re.compile('<tr>.*?<td style="text-align: left.*?>(.*?)</td>.*?<td style="text-align: left.>'+
    					'(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>.*?<a.*?style'+
    					'="cursor: pointer".*?onclick="queryMoreDwList.*?>(.*?)</a></td>',re.S)
    items = re.findall(pattern,content)
    for item in items:
    	print item[0]+'----'+item[1]+'---'+item[2]+'---'+item[3]+'---'+item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason