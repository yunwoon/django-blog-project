from django.shortcuts import render
from django.utils import timezone
from .models import Portfolio
# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    portfolios.pub_date = timezone.datetime.now()
    return render(request,'portfolio.html',{'portfolios':portfolios})