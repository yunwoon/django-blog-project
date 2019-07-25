from django.shortcuts import render

from django.contrib.auth.models import User #user에 대한 클래스 가져옴
from django.contrib import auth #권한에 관한

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            auth.login(request, user)
            return redirect('index') #위에 있는 게 전부 실행 -> index페이지로 가자
    return render(request, 'signup.html') #아니라면 가만히 있어

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: #회원 명단에 있다면
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'login.html')