# -*- coding: cp936 -*-  
import WebCrawler  

url = raw_input('�������url(��-->http://www.baidu.com): \n')  
thNumber = int(raw_input('�����߳���:'))    #֮ǰ����δת����bug  
Maxdepth = int(raw_input('���������ȣ�'))  
wc = WebCrawler.WebCrawler(thNumber, Maxdepth)  
wc.Craw(url)  

