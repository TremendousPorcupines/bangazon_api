from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
import json

def register_user(request):
    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'],
        password=req_body['password'],
        email=req_body['email'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        )

    new_user.save()
    return login_user(request)

def login_user(request):
    req_body = json.loads(request.body.decode())

    authenticated_user = authenticate(
        username=req_body['username'],
        password=req_body['password']
        )

    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)
    else:
        success = False

    data = json.dumps({"success":success})
    return HttpResponse(data, content_type='application/json')

def logout_user(request):
    logout(request)
    return HttpResponse(True)


def userAuth(request):
    if request.user.is_anonymous:
        response = json.dumps({"user": False})
    else:
        response = json.dumps({
            "user": True,
            "user_id":request.user.pk,
            "username": request.user.first_name
        })
    return HttpResponse(response, content_type='application/json')
