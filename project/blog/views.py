from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone #현재 시점을 받아와주기 위해 임포오트!
from .models import Blog

# Create your views here.
def index(request):
    return render(request,'index.html')

def board(request):
    blogs = Blog.objects
    return render(request,'board.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail =  get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):  #new.html띄어주는 함수
    return render(request,'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']     #blog 객체 안에 title 변수에 넣어준다
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()    #블로그를 작성하는 시점을 넣어주는 함수
    blog.save()   #블로그라는 객체에 데이터를 넣었자너 / 그 객체를 데이터베이스에 저장하는게 .save() 메소드임!!
                  #객체.delete() 는 객체에 해당하는 내용을 데베로부터 지워라!
    return redirect('/board/detail/'+str(blog.id)) #위에 함수들을 다 처리하고 써진 url로 이동,넘겨지는 거임
    #blog.id는 int형이지만 url은 항상 문자형이기 때문에 str로 형변환을 해줌
