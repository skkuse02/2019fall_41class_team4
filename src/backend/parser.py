from urllib.request import urlopen
from bs4 import BeautifulSoup

class Parser():
	def __init__(self, _url):
		self.m_url = _url
		self.m_tags = [] 
	
	def openUrl(self):
		_html = urlopen(self.m_url)
		_bs_object = BeautifulSoup(_html, "html.parser")
		return _bs_object

	def parseItem(self):
		_bs_object = self.openUrl()
		print(_bs_object.find(class_='price_real').get_text())
