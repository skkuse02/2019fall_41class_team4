from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .parserer import Parserer
import json

@csrf_exempt
# Create your views here.
def control(_request):
	_response = select(_request)
	print(_response)
	return JsonResponse(_response)

def select(_request): 
	_path = _request.path
	_rawdata = _request.body.decode('utf-8')

	try:
		_data = json.loads(_rawdata)
		print(_data)
	except:
		_response = {'status':'fail', 'message':'Request form error'}
		return _response

	_parserer = Parserer(_data)
	
	if 'item' in _path:
		print("[Item Status]")
		try:
			_response = _parserer.parseItem()
			_response['status'] = 'success'
			_response['message'] = 'Item parse success'
		except:
			_response = {}
			_response['status'] = 'fail'
			_response['message'] = 'This shopping mall site is not supported'	
		return _response

	if 'review' in _path:
		print("[Review Status]")
		try:
			_response = _parserer.parseReview()
			_response['status'] = 'success'
			_response['message'] = 'Review parse success'
		except:
			_response = {}
			_response['status'] = 'fail'
			_response['message'] = 'This item does not support review'
		return _response
