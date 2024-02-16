from django.shortcuts import redirect
from django.urls import reverse
import time
import jwt

def token_decode(token):
    try:
        decoded_token = jwt.decode(token, options={'verify_signature': False}, algorithms=['HS256'])
        print("Decoded Token:", decoded_token)
        return decoded_token
    except jwt.ExpiredSignatureError:
        print('Token has expired')
    except jwt.DecodeError:
        print('Token Could Not Be Decoded')

def login_required(view_func):
    
    def _wrapped_view(request, *args, **kwargs):
        token = request.session.get('Token')
        now = time.time() 
        if token is not None:
            resp = token_decode(token)
            exp = resp['exp']
            if now > exp:
                request.session['next'] = request.get_full_path()
                return redirect(reverse('login')) 
        else:
            request.session['next'] = request.get_full_path()
            return redirect(reverse('login'))

        return view_func(request, *args, **kwargs)
    return _wrapped_view