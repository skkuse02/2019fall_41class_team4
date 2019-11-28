class Product:
	def __init__(self):
		self.m_url = None
		self.m_domain = None
		self.m_name = None
		self.m_price = None
		self.m_image = None
	
	def printItem(self):
		print("Item Url: " + self.m_url)
		print("Item Doamin: " + self.m_domain)
		print("Item Name: " + self.m_name)
		print("Item Price: " + self.m_price)
		print("Item Image: " + self.m_image)
		print(" ")
	
	def setUrl(self, _url):
		self.m_url = _url
	
	def setDomain(self, _domain):
		self.m_domain = _domain

	def setName(self, _name):
		self.m_name = _name

	def setPrice(self, _price):
		self.m_price = _price

	def setImage(self, _image):
		self.m_image = _image

	def getUrl(self):
		return self.m_url

	def getDomain(self):
		return self.m_domain

	def getName(self):
		return self.m_name

	def getPrice(self):
		return self.m_price

	def getImage(self):
		return self.m_image
