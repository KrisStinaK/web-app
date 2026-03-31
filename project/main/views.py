from django.shortcuts import render
from news.models import Articles

def index(request):
    news = Articles.objects.order_by('-id')[:3]
    news_p = Articles.objects.order_by('-id')[3:]
    data = {
        'title': 'Главная страница',
        'news': news,
        'news_p': news_p,
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
