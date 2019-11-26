class Authenticator:
	def __init__(self):
		self.m_id = None
		self.m_pw = None

		def loginUser(self): 
			# validate id, pw
			pass

		def registerUser(self):
			# register new user
			pass

		def setId(self, _id): 
			self.m_id = _id
		
		def setPw(self, _pw):
			self.m_pw = _pw

		def getId(self):
			return self.m_id

		def getPw(self):
			return self.m_pw
