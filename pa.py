#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'brucezheng'
#对学校的就业信息网，招聘会信息进行采集
import urllib
import urllib2
import re

#page = 1
#url = 'http://www.qiushibaike.com/hot/page/' + str(page)
class pa_jobs():
    """用来抓取seu就业网站上面的信息"""
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }

    def getPages(self):
        try:
            url = 'http://jy.seu.edu.cn/detach.portal?.pen=pe781&.pmn=view&action=queryAllZphManageView'
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
          #  pattern = re.compile('<a.*?style="cursor: pointer".*?onclick="queryMoreDwList.*?>(.*?)</a>',re.S)
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接web失败,错误原因",e.reason
                return None   
    def getPagesItems(self):
        content = self.getPages()
        if not content:
            print "页面加载失败...."
            return None
        try:
            pattern = re.compile('<tr>.*?<td style="text-align: left.*?>(.*?)</td>.*?<td style="text-align: left.>'+
            					'(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>.*?<a.*?style'+
            					'="cursor: pointer".*?onclick="queryMoreDwList.*?>(.*?)</a></td>',re.S)
            items = re.findall(pattern,content)
            for item in items:
                # print '''________________________________________________________________________________________________________________________'''
            	print item[0]+'----'+item[1]+'---'+item[2]+'---'+item[3]+'---'+item[4]
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason

    def start(self):
        print '''开始运行SEU_Jobs信息采集系统...'''
        input = raw_input('键入回车继续')
        self.getPagesItems()


spider = pa_jobs()
spider.start()