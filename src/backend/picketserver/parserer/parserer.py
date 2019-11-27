from urllib.request import urlopen
from bs4 import BeautifulSoup

class Parserer:

	def __init__(self, _url):
		self.m_url = _url
		self.m_tags = {'domain_tag':'', 'name_tag':'', 'price_tag':'', 'image_tag':''}
	
	def openUrl(self):
		_html = urlopen(self.m_url)
		_bs = BeautifulSoup(_html, 'html.parser')
		return _bs
	
	def parseItem(self):
		_bs = self.openUrl()

		# get Item Name
		_name = _bs.find(class_ = 'itemtit').get_text()

		# get Item price
		_price = _bs.find(class_ = 'price_real').get_text()

		# get Item Image
		_img = _bs.select('li > a > img')
		_img = _img[0].get('src')

		return {'name':_name, 'price':_price, 'image':_img}

	def parseReview(self):
		_bs = self.openUrl()
		pass

	def recvTag(self):
		pass

	def setUrl(self,_url):
		self.m_url = _url
	
	def setTags(self, _tags):
		self.m_tags = _tags

	def getUrl(self):
		return self.m_url
	
	def getTags(self):
		return self.m_tags
