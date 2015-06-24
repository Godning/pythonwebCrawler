import urllib2
import urllib
import re
import time
import os
import uuid

#��ȡ����ҳ��url
def findUrl2(html):
    re1 = r'http://tuchong.com/\d+/\d+/|http://\w+(?<!photos).tuchong.com/\d+/'
    url2list = re.findall(re1,html)
    url2lstfltr = list(set(url2list))
    url2lstfltr.sort(key=url2list.index)
    #print url2lstfltr
    return url2lstfltr

#��ȡhtml�ı�
def getHtml(url):
    html = urllib2.urlopen(url).read().decode('utf-8')#����Ϊutf-8
    return html

#����ͼƬ������
def download(html_page , pageNo):   
    #�����ļ��е�����
    x = time.localtime(time.time())
    foldername = str(x.__getattribute__("tm_year"))+"-"+str(x.__getattribute__("tm_mon"))+"-"+str(x.__getattribute__("tm_mday"))
    re2=r'http://photos.tuchong.com/.+/f/.+\.jpg'
    imglist=re.findall(re2,html_page)
    print imglist
    download_img=None
    for imgurl in imglist:
        picpath = 'L:\\photo\\%s\\%s'  % (foldername,str(pageNo))
        filename = str(uuid.uuid1())
        if not os.path.exists(picpath):
            os.makedirs(picpath)               
        target = picpath+"\\%s.jpg" % filename
        print "The photos location is:"+target
        download_img = urllib.urlretrieve(imgurl, target)#��ͼƬ���ص�ָ��·����
        time.sleep(1)
        print(imgurl)
    return download_img

# def callback(blocknum, blocksize, totalsize):
#     '''�ص�����
#     @blocknum: �Ѿ����ص����ݿ�
#     @blocksize: ���ݿ�Ĵ�С
#     @totalsize: Զ���ļ��Ĵ�С
#     '''
#     print str(blocknum),str(blocksize),str(totalsize)
#     if blocknum * blocksize >= totalsize:
#         print '�������'

def quitit():
    print "Bye!"
    exit(0)
    

if __name__ == '__main__':
    print '''            *****************************************
            **    Welcome to Spider for TUCHONG    **
            **      Created on 2014-4-24           **
            **      @author: Leon Wong             **
            *****************************************'''
    pageNo = raw_input("Input the page number you want to scratch (1-100),please input 'quit' if you want to quit>")
    while not pageNo.isdigit() or int(pageNo) > 100 :
        if pageNo == 'quit':quitit()
        print "Param is invalid , please try again."
        pageNo = raw_input("Input the page number you want to scratch >")

    #���ͼ������ģ������ȡ
    html = getHtml("http://tuchong.com/tags/%E4%B9%9D%E5%AF%A8%E6%B2%9F/?page="+str(pageNo))

    detllst = findUrl2(html)
    for detail in detllst:
        html2 = getHtml(detail)
        download(html2,pageNo)
    print "Finished."
