from django.db import models
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) #문자 데이터를 title로 정의함
    pub_date = models.DateTimeField('date_published') #날짜 시간 데이터를 정의
    body = models.TextField() #charfield보다 더 긴 field

    def __str__(self): #타이틀이 블로그 제목으로 써지게 함
        return self.title
        
    def summary(self):
        return self.body[:100]