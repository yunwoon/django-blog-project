from django.shortcuts import render, redirect

from django.contrib.auth.models import User #user에 대한 클래스 가져옴
from django.contrib import auth #권한에 관한

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': '이미 존재하는 사용자입니다!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], email=request.POST['useremail'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다!'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')

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