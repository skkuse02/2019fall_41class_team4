from .models import User

class Authenticator:
	def __init__(self):
		self.m_id = None
		self.m_pw = None
		self.m_email = None

		def loadData(self, _rawdata):
			try:
				_data = json.loads(_rawdata)
				self.m_id = _data['user_id']
				self.m_pw = _data['user_pw']
				self.m_email = _data['user_email']
			except:
				return 0, "Request Error"
            
		def validateUser(self): 
			# validate id, pw
			try:
				user = User.objects.get(user_id = self.m_id)
			except:
				return 0, "If this is your fisrt time visiting, please sign up first."

			if user.user_pw == self.m_pw: 
				return 1, "You have successfuly logged in."
			else:
				return 0, "You have entered wrong password."
			pass

		def registerUser(self):
			# register new user
			try:
				User.objects.get(user_id = self.m_id)
				return 0, "This ID is already in Use. Please re-enter."
			except:
				user = User(user_id = self.m_id, user_pw = self.m_pw)
				user.save()
				# ??? send registration email to user ??? 
				return 1, "You have successfully registered."			

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
