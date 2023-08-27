from django.shortcuts import render , redirect
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, get_user_model




# Create your views here.

def lobby(request):
    return render(request, 'base/lobby.html')

# def index(request):
#     return render(request, 'base/index.html')

def room(request):
    return render(request, 'base/room.html')



def register(request):
    print('in register')
    print(request)
    if request.method == "POST":
        print('inpost')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('uname')
        
        print(username)
        # user = authenticate(email = email,password =password)
        user = User.objects.create_user(username, email, password)
        message ='signup successfully'
    else:
        print('not post')
        return render(request, 'base/register.html')

        
        
    
def main(request):
    return render(request,'main.html')

def studentd(request):
    return render(request, 'studentd.html')


def login(request):
    
    if request.user.is_authenticated:
        return redirect('main')
       
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = User.objects.get(email=email).username
        # user_id = User.objects.get(email=email).id
        # data = {
        #     'username':username,
        #     'eamil':email,
        #     'user_id':user_id,
        # }
        # print(data)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('main')
    else:
        return redirect('login.html')
              
    return render(request, 'base/login.html')

    
    
    return render(request, 'base/login.html')

def getToken(request):
    appId = "6bb17f29e6484385bd9cd18f62d29512"
    appCertificate = "7d419c13e18d458c8a4a405540446568"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)