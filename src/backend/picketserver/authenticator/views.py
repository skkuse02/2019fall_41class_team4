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
	authenticator.setId()
	# try to load json
#	try: 
#		_data = json.loads(_rawdata)
#	except:
#		_response = {'status':'fail', 'message':'json error'}
#		return _response
	
	# retreive info from request
#	_id = _data['id']
#	_pw = _data['pw']
#	_email = _data['email']

	# set user info
#	authenticator.setId(_id)
#	authenticator.setPw(_pw)
#	authenticator.setEmail(_email)

	# select appropriate function
	if 'login' in _path:
		print("[Login Status]")
		_status, _message = authenticator.validateUser()
	if 'register' in _path:
		print("[Register Status]")
		_status, _message = autehnticator.registerUser()
	
	if _status == 0:
		_status = 'fail'
	else:
		_status = 'success'

	_response = {'status':_status, 'message':_message}
	return _response
