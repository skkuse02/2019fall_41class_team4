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
	authenticator = Authenticator()
	_path = _request.path
	_rawdata = _request.body.decode('utf-8')

	try: 
		_data = json.loads(_rawdata)
	except:
		_response = {'status':'json_error'}
		return _response

	_id = _data['id']
	_pw = _pw['pw']
	authenticator.setId(_id)
	authenticator.setPw(_pw)

	if 'login' in _path:
		print("[Login Status]")
	if 'register' in _path:
		print("[Register Status]")
	
