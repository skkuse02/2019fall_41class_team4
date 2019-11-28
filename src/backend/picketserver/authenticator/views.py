from django.http import HttpResponse, JsonResponse
from .authenticator import Authenticator
import json

# Create your views here.
def control(_request):
	print(_request)
	_response = select(_request)
	print(_response)

	return JsonResponse(_response)

def select(_request):
	_path = _request.path
	_rawdata = _request.body.decode('utf-8')
	
	# try to load JSON
	try:
		_data = jsons.loads(_rawdata)
	except:
		_response = {'status':'fail', 'message':'Request format error'}
		return _response
	
	
	authenticator = Authenticator()
	authenticator.retrieveUser(_data)

	# select appropriate function
	if 'login' in _path:
		print("[Login Status]")
		_status, _message = authenticator.validateUser()
	if 'register' in _path:
		print("[Register Status]")
		_status, _message = authenticator.registerUser()
	if 'loadcart' in _path:
		print("[Load Cart]")
		_status, _message = authenticator.loadCart()
	if 'savecart' in _path:
		print("[Save Cart]")
		_status, _message = authenticator.saveCart(_data)


	_response = {'status':_status, 'message':_message}
	return _response
