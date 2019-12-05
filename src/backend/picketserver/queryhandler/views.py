from django.http import HttpResponse, JsonResponse
from .queryhandler import QueryHandler
from django.views.decorators.csrf import csrf_exempt
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
		_response = {'status':'fail', 'message':'Request format error'}
		return _response
  
	_queryhandler = QueryHandler()
	if 'domainquery' in _path:
		print("[Domain Query]")
		_response = _queryhandler.queryDomain(_data)
	if 'elsequery' in _path:
		print("[Else Query]")
		_response = _queryhandler.queryElse(_data)

	return _response

