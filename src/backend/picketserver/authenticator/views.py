from django.http import HttpResponse, JsonResponse
from .authenticator import Authenticator
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
  	
	# try to load JSON
	try:
		_data = json.loads(_rawdata)
		print(_data)
	except:
		_response = {'status':'fail', 'message':'Request format error'}
		return _response
	
	
	authenticator = Authenticator()
	authenticator.retrieveUser(_data)

	# select appropriate function
	if 'login' in _path:
		print("[Login Status]")
		_response = authenticator.validateUser()
	if 'register' in _path:
		print("[Register Status]")
		_response = authenticator.registerUser()
	if 'loadcart' in _path:
		print("[Load Cart]")
		_response = authenticator.loadCart()
	if 'savecart' in _path:
		print("[Save Cart]")
		_response = authenticator.saveCart(_data)

	return _response
