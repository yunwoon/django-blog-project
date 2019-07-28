from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone #현재 시점을 받아와주기 위해 임포오트!
from django.core.paginator import Paginator #pagination 을 위해 임포오트!
from .models import Blog
from .form import BlogPost

# Create your views here.
def index(request):
    return render(request,'index.html')

def board(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all() #블로그의 모든 글을 대상으로
    paginator = Paginator(blog_list, 3) #블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page') #request된 페이지가 뭔지 알아내고 (request페이지를 변수에 담고)
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤 return 해 준다
    return render(request,'board.html',{'blogs':blogs, 'posts':posts})

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

def blogpost(request):
    #1.입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #저장하지 않고 model 객체를 가져옴 (post는 블로그형 객체)
            post.pub_date = timezone.now()
            post.save()
            return redirect('board')

    #2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def place(request):
    return render(request,'place.html')