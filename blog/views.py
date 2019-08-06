from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from blog.models import Article, Comment 

def root(request):
    return HttpResponseRedirect("index")

def index(request):
    article = Article.objects.all()
    context = {
      'current_time': datetime.now(),
      "articles": article
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def show(request, id):
    article = Article.objects.get(pk=id)
    context = {"article": article}
    return render(request, 'show.html', context)

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.filter(id=article_id)[0]
    name = request.POST['name']
    message  = request.POST['message']
    comment = Comment(name=name, message=message, article=article)
    comment.save()
    print(article)
    return HttpResponseRedirect('/index/' + article_id)