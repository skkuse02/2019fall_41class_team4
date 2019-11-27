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
		_name = _bs_object.find(class_='itemtit').get_text()
		print(_name)
	  
		_img = _bs_object.select('li > a > img')
		
		_domain = _bs_object.find(class_='sprite__common')
		_domain = _bs_object.select('span')
		print(_domain)
