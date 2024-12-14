from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News


def home(request):
    return render(request, 'home.html')


def news(request):
    news = News.objects.all().order_by('date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'news.html', context)
