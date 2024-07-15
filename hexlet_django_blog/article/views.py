from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


    def article_view(request, tag, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tag}')