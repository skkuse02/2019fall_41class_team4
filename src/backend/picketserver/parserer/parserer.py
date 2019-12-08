import sys
import math
import re
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
from .models import Tag, RTag
from model_loader import run_model

class Parserer:

	def __init__(self, _data):
		self.m_url = _data['item_url']
		self.m_domain = None
		self.m_tags = {'item_domain':'', 'name_tag':'', 'price_tag':'', 'image_tag':''}
		self.m_rtags = {'pagenum_tag':'', 'review_tag':''}

	def openUrl(self):
		_html = urlopen(self.m_url)
		_bs = BeautifulSoup(_html, 'html.parser')
		return _bs
	
	def openWebdriver(self):
		_options = webdriver.ChromeOptions()
		_options.add_argument('headless')
		
		_driver = webdriver.Chrome('/home/ubuntu/2019fall_41class_team4/src/backend/picketserver/parserer/chromedriver', options=_options)
		_driver.get(self.m_url)
		return _driver

	def parseDomain(self):
		_list = self.m_url.split('.')

		try:
			_index = _list.index('co') - 1
			self.m_domain = _list[_index]
			return
		except:
			pass

		try:
			self.m_domain = _list[1]
			return
		except:
			pass

		self.m_domain = 'null'
	
	def parseItem(self):
		self.parseDomain()
		self.recvTags()
		_bs = self.openUrl()

		# get Item Name
		exec(self.m_tags['name_tag'])
		self._name = self._name.strip()

		# get Item price
		exec(self.m_tags['price_tag'])
		self._price = self._price.split('원')[0]

		# get Item Image
		exec(self.m_tags['image_tag'].encode('ascii').decode('unicode-escape'))

		return {'domain_name':self.m_tags['item_domain'], 'item_url':self.m_url, 'item_name':self._name, 'item_price':self._price, 'item_image':self._img}

	def parseReview(self, _driver):
		self.parseDomain()
		self.recvRTags()
		self._driver = _driver
		self._driver.get(self.m_url)
		self._list = [] # review list
	
		# get page number 
		try:
			exec(self.m_rtags['pagenum_tag'].encode('ascii').decode('unicode-escape'))
		except:
			return {'status':'none', 'message':'no review'}

		if self._pagenum == 0:
			return {'status':'none', 'message':'no review'}
		if self._pagenum > 5:
			self._pagenum = 5

		# get reviews	
		exec(self.m_rtags['review_tag'].encode('ascii').decode('unicode-escape'))
		
		# run machine learning	
		self._class = None # classification list
		try:
		# machine learning save at self._class, data is in _list
			self._class = run_model(self._list)
		except:
			self._class = [0] * len(self._list)
			pass

		_positive = []
		_negative = []
		for i in range(len(self._list)):
			if self._class[i] == 0:
				_positive.append(self._list[i])
			else:
				_negative.append(self._list[i])
		return {'positive_review':_positive, 'negative_review':_negative}

	def recvTags(self):
		tag = Tag.objects.get(domain_name = self.m_domain)
		self.m_tags['item_domain'] = tag.tag_domain
		self.m_tags['name_tag'] = tag.tag_name
		self.m_tags['price_tag'] = tag.tag_price
		self.m_tags['image_tag'] = tag.tag_image
	
	def recvRTags(self):
		rtag = RTag.objects.get(domain_name = self.m_domain)
		self.m_rtags['pagenum_tag'] = rtag.tag_pagenum
		self.m_rtags['review_tag'] = rtag.tag_review

	def setUrl(self,_url):
		self.m_url = _url
	
	def setTags(self, _tags):
		self.m_tags = _tags

	def getUrl(self):
		return self.m_url
	
	def getTags(self):
		return self.m_tags
