from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .parserer import Parserer
import json

@csrf_exempt
# Create your views here.
def control(_request):
	_response = select(_request)
	print(_response)
#_response.encode('utf-8')
	return JsonResponse(_response)

def select(_request): 
	_path = _request.path
	_rawdata = _request.body.decode('utf-8')

	try:
		_data = json.loads(_rawdata)
		print(_data)
	except:
		_response = {'status':'fail', 'message':'Request form error'}

	parserer = Parserer(_data)
	parserer.parseDomain()
	parserer.recvTags()
	
	if 'item' in _path:
		print("[Item Status]")
		try:
			_response = parserer.parseItem()
			_response['status'] = 'success'
			_response['message'] = 'Item parse success'
		except:
			_response = {}
			_response['status'] = 'fail'
			_response['message'] = 'This shopping mall site is not supported'	
		return _response

	if 'review' in _path:
		print("[Review Status]")
		return praserer.parseReview()
