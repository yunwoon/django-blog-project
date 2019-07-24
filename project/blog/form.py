#models.py 안에 있는 블로그 클래스를 기반으로 공간을 만들 것이기에 같은 폴더 내에 form.py 만듦
#위치는 그렇게 중요하지 않다
from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): #모델 폼 기반
    class Meta:
        model = Blog
        fields = ['title', 'body']

class BlogPost2(forms.Form): #임의의 공간
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])