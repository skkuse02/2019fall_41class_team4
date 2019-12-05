from .product import Product
from .models import Item, User

class Cart:
	def __init__(self, _id):
		self.m_items = []
		self.m_id = _id

	def makeCart(self, _data):			
		_cart = _data['user_cart']

		for item in _cart:
			_item = Product()
			_item.setUrl(item['item_url'])
			_item.setDomain(item['item_domain'])
			_item.setName(item['item_name'])
			_item.setPrice(item['item_price'])
			_item.setImage(item['item_image'])
			
			self.m_items.append(_item)
	
	def saveCart(self):
		_user = User.objects.get(user_id = self.m_id) # to check is registered user
		self.deleteCart() # necessary?

		for item in self.m_items:
			_item = Item(user_id = _user, item_url = item.getUrl(), 
					item_domain = item.getDomain(), item_name = item.getName(),
					item_price = item.getPrice(), item_image = item.getImage())
			_item.save()

	def loadCart(self):
		_user = User.objects.get(user_id = self.m_id) # to check is registered user
		_items = Item.objects.filter(user_id = self.m_id)

		for item in _items:
			_item = Product()
			_item.setUrl(item.item_url)
			_item.setDomain(item.item_domain)
			_item.setName(item.item_name)
			_item.setPrice(item.item_price)
			_item.setImage(item.item_image)
			
			self.m_items.append(_item)

	def deleteCart(self):
		_items = Item.objects.filter(user_id = self.m_id).delete()
	
	def dictCart(self):
		_list = []
		for item in self.m_items:
			_dict = {}
			_dict['item_url'] = item.getUrl()
			_dict['item_domain'] = item.getDomain()
			_dict['item_name'] = item.getName()
			_dict['item_price'] = item.getPrice()
			_dict['item_image'] = item.getImage()
			
			_list.append(_dict)
		
		_response = {}
		_response['user_id'] = self.m_id
		_response['user_cart'] = _list

		return _response

	def printCart(self):
		print("User ID: " + self.m_id)
		print("")
		for item in self.m_items:
			item.printItem()
