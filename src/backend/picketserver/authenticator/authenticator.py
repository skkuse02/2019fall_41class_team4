from .models import User
from .cart import Cart

class Authenticator:
	def __init__(self):
		self.m_id = None
		self.m_pw = None
		self.m_email = None
		self.m_cart = None

	def retrieveUser(self, _data):
		try:
			self.m_id = _data['user_id']
			self.m_pw = _data['user_pw']
			self.m_email = _data['user_email']
		except:
			pass
            
	def validateUser(self):
		# validate id, pw
		try:
			user = User.objects.get(user_id = self.m_id)
		except:
			return {"status":"fail", "message": "If this is your fisrt time visiting, please sign up first."}

		if user.user_pw == self.m_pw: 
			return {"status":"success", "message":"You have successfully logged in."}
		else:
			return {"status":"fail", "message":"You have entered wrong password."}
		pass

	def registerUser(self):
		# register new user
		try:
			User.objects.get(user_id = self.m_id)
			return {"status":"fail", "message":"This ID is already in Use. Please re-enter."}
		except:
			user = User(user_id = self.m_id, user_pw = self.m_pw)
			user.save()
			# ??? send registration email to user ??? 
			return {"status":"success", "message":"You have successfully registered."}		

	def loadCart(self):
		try:
			_cart = Cart(self.m_id)
			_cart.loadCart()
			_dict = _cart.dictCart()
		except:
			return {"status":"fail", "message":"Fail to load cart"}

		_dict['status'] = "success"
		_dict['message'] = "Cart is lodded"
		return _dict

	def saveCart(self, _data):
		try:
			_cart = Cart(self.m_id)
			_cart.makeCart(_data)
			_cart.saveCart()
			return {"status":"success", "message":"Cart is saved."}
		except: 
			return {"status":"fail", "message":"Cart save failed. Please try again"}

	def setId(self, _id): 
		self.m_id = _id
		
	def setPw(self, _pw):
		self.m_pw = _pw
		
	def setEmail(self, _emal):
		self.m_email = _email

	def getId(self):
		return self.m_id

	def getPw(self):
		return self.m_pw

	def getEmail(self):
		return self.m_email
