from .models import QueryDomain, QueryElse

class QueryHandler:
	def __init__(self):
		self.m_url = None
		self.m_domain = None
		self.m_comment = None

	def parseDomain(self):
		_list = self.m_url.split('.')
		
		try:
			_index = _list.index('co') - 1
			self.m_domain = _list[_index]
			return
		except:
			pass

		try:
			_index = _list.index('com') - 1
			self.m_domain = _list[_index]
			return
		except:
			pass

		self.m_domain = 'null'

	def queryDomain(self, _data):
		self.m_url = _data['query_url']
		self.parseDomain()
			
		try:
			domainquery = QueryDomain(original_url = self.m_url, domain_url = self.m_domain)
			domainquery.save()
			return {"status":"success", "message":"Domain query accepted"} 
		except:
			return {"status":"fail", "message":"Not valid url"}

	def queryElse(self, _data):
		self.m_comment = _data['query_comment']

		try:
			elsequery = QueryElse(user_comment = self.m_comment)
			elsequery.save()
			return {"status":"success", "message":"Else query accepted"}
		except:
			return {"status":"fail", "message":"Else query DB error"}
