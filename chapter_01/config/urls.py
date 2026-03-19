"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import responses

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render

movie_list = [
    {'title': '왕과 사는 남자', 'director': '왕'},
    {'title': '프로젝트 헤일메리', 'director': '헤일메리'},
    {'title': '메소드 연기', 'director': '배우'},
    {'title': '호퍼스', 'director': '호퍼'},
    {'title': '폭탄', 'director': '폭탄광'},
]

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def book_list(request):
    # book_text = ''
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'
    # return HttpResponse(book_text)
    return render(request, 'book_list.html', {'range': range(1, 11)})


def book(request, num):
    # book_text = f'book {num}번 페이지입니다.'
    # return HttpResponse(book_text)
    return render(request, 'book_detail.html', {'num': num})

def language(request, lang):
    return HttpResponse(f"<h1>{lang} 언어 페이지입니다.")

def movies(request):
    # movie_titles = [movie['title'] for movie in movie_list]
    # response_text = ''
    # for index, title in enumerate(movie_titles):
    #     response_text += f'<a href="/movie/{index}/">{title}</a><br>'

    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie["title"]}</a>'
    #     for index, movie in enumerate(movie_list)
    # ]
    # response_text = ''
    # response_text += '<br>'.join(movie_titles)

    # return HttpResponse(response_text)
    return render(request, 'movies.html', {'movie_list': movie_list})


def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    # movie = movie_list[index]
    context = {'movie' : movie}

    return render(request, 'movie.html', context)

def gugu(request, num):
    context = {
        'num' : num,
        'results' : [num * i for i in range(1, 10)]
    }

    return render(request, 'gugu.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('book_list/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('gugu/<int:num>/', gugu),
]
