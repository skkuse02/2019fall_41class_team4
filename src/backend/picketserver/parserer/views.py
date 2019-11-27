from django.http import HttpResponse, JsonResponse
from .parserer import Parserer
import json

# Create your views here.
def control(_request):
	_response = select(_request)
	return JsonResponse(_response)

def select(_request): 
	_path = _request.path
	_rawdata = _request.body.decode('utf-8')


	parserer = Parserer("http://item.gmarket.co.kr/Item?goodscode=1175120632&ver=637104594321172559")
	
	if 'item' in _path:
		print("[Item Status]")
		return parserer.parseItem()
	if 'review' in _path:
		print("[Review Status]")
		return praserer.parseReview()
