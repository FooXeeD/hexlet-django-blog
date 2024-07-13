from django.shortcuts import render
 
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={
            'tag': 'python', 'article_id': 42
        }))


    def article_view(request, tag, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tag}')