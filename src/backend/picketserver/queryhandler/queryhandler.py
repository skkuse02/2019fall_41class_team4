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
			self.m_domain = _lint[_index]
			return
		except:
			pass

	def queryDomain(self, _data):
		self.m_url = _data['query_url']
		parseDomain()

		domainquery = QueryDomain('original_url' = self.m_url, 'domain_url' = self.m_domain)
		domainquery.save()

	def queryElse(self, _data):
		self.m_comment = _data['query_comment']

		elsequery = QueryElse('user_comment' = self.m_comment)
