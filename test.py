# -*- coding: cp936 -*-  
import WebCrawler  

url = raw_input('设置入口url(例-->http://www.baidu.com): \n')  
thNumber = int(raw_input('设置线程数:'))    #之前类型未转换出bug  
Maxdepth = int(raw_input('最大搜索深度：'))  
wc = WebCrawler.WebCrawler(thNumber, Maxdepth)  
wc.Craw(url)  

