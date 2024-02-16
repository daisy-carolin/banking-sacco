from django.shortcuts import render,redirect
from django.urls import resolve,reverse
import jwt
from sub_part.api_call import *
import json
import requests
from django.contrib import messages

BASE_URL='http://127.0.0.1:8001/backend/v1'

# Create your views here.

def token_decode(token):
    try:
        decoded_token = jwt.decode(token, options={'verify_signature': False}, algorithms=['HS256'])
        print("Decoded Token:", decoded_token)
        return decoded_token
    except jwt.ExpiredSignatureError:
        print('Token has expired')
    except jwt.DecodeError:
        print('Token Could Not Be Decoded')
        
def login(request, next_url=None):
    next_url = request.session.get('next') 
    print(next_url)
    print('next url for login dash')

    if request.method == 'POST':
        print('It is post')
        endpoint = "token/"
        payload = {
            'phone_number': request.POST.get('phone_number'),
            'password': request.POST.get('password')
        }
        json_data = json.dumps(payload)
        response = call_post_without_token(BASE_URL, endpoint, json_data)
        
        if response.status_code != 200:
            print('response ', response.json())
            print('respone ', response)
            print(response.json().get('detail'))
            print('Response is not 200')
            messages.error(request, str(response.json().get('detail')), extra_tags='error')
            return render(request, 'Auth/login.html')
        else:
            print('response ', response.json())

            #set the token
            request.session['Token'] = response.json()['access']
            #decode
            dec_resp = token_decode(response.json()['access'])
            request.session['user_id'] = dec_resp['user_id']
           
            print('respone ', response)
            if next_url:
                url = resolve(next_url)
                print('url name', url.url_name)
                return redirect(url.url_name)
            else:
                return redirect('home')
            
    if request.user.is_authenticated:
        # Display a logout link when the user is signed in
        logout_link = f'<a href="{reverse("logout")}">Logout</a>'
    else:
        logout_link = ''

    # Render the template with the logout link (if applicable)
    context = {
        'logout_link': logout_link,
    }
    
    return render(request, 'Auth/login.html')
            

def index(request):
    return render(request, 'CreateGroup/index.html')

def register(request):
    return render(request, 'Auth/register.html')

def home(request):
    return render(request, 'Basic/home.html')

def join_group(request):
    return render(request, 'Basic/join_group.html')

def proceed(request):
    return render(request, 'Basic/proceed.html')

def create_group(request):
    return render(request, 'CreateGroup/create_group.html')

def member_contribution(request):

    return render(request, 'Basic/member_contribution.html')

def view_member_contribution(request):
    return render(request, 'Basic/view_member_contribution.html')

def borrow_loan(request):
    return render(request, 'Basic/borrow_loan.html')

def borrow_loan_view(request):
    return render(request, 'Basic/borrow_loan_view.html')

def fund_loan(request):
    return render(request, 'Basic/fund_loan.html')

def fund_loan_add(request):
   
    return render(request, 'Basic/fund_loan_add.html')

def repay_loan(request):
    return render(request, 'Basic/repay_loan.html')

def repay_loan_add(request):
    return render(request, 'Basic/repay_loan_add.html')

def viewapi(request):
    api_url = 'http://127.0.0.1:2332/api_Institution'
    response = requests.get(api_url)
    api_data = response.json()  # Assuming your API returns JSON data
    print(api_data)
    context={
        'api_data':api_data['data']
    }
    return render(request, 'CreateGroup/viewapi.html',context)