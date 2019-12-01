from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def control(_request):
	print(_request)
	_response = select(_request)
	print(_response)

	return JsonResponse(_response)

def select(_request):
	_path = request.path 
	_rawdata = _request.body.decode('utf-8')

	try:
	  _data = jsons.loads(_rawdata)
	except:
	  _respons = {'status':'fail', 'message':'Request format error'}

