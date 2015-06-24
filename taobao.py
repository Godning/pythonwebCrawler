import urllib2
from sgmllib import SGMLParser

class ListName1(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h4 = ""
		self.name = []
	def start_h4(self, attrs):
		self.is_h4 = 1
	def end_h4(self):
		self.is_h4 = ""
	def handle_data(self, text):
		if self.is_h4 == 1:
			self.name.append(text)
			
class ListName2(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h5 = ""
		self.name = []
	def start_h5(self, attrs):
		self.is_h5 = 1
	def end_h5(self):
		self.is_h5 = ""
	def handle_data(self, text):
		if self.is_h5 == 1:
			self.name.append(text)
 
content = urllib2.urlopen('http://list.taobao.com/browse/cat-0.htm').read()

listname1 = ListName1()
listname2 = ListName2()
listname1.feed(content)
listname2.feed(content)
for item in listname1.name:
	print item

for item in listname2.name:
	print item
#http://list.taobao.com/browse/cat-0.htm