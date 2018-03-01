from django.shortcuts import render
from .models import Article, Author, Comment
from django.http import HttpResponseNotFound
from .forms import ArticleForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def index(request):
    articles = Article.objects.all()
    comments = Comment.objects.all()
    return render(request, 'news_blog/news_list.html', {'articles':articles})
articles = [
   {
       'id': 1,
       'title': 'OH MY GOD',
       'text': 'This is demo of sequencing guide'
   },
   {
       'id': 2,
       'title': 'SO I LIKE THIS SHIT',
       'text': 'DNA is a trash'
   },
{
       'id': 3,
       'title': 'IT IS HARD',
       'text': 'But it is ok'
   }]
def get_article(request, article_id):
   try:
       article = Article.objects.get(id=article_id)
       author = Author.objects.filter(article__pk=article_id)
       comment = Comment.objects.filter(article=article)
   except (Article.DoesNotExist, Author.DoesNotExist, Comment.DoesNotExist) as error:
       return HttpResponseNotFound(error)
   return render(request, 'news_blog/news_article.html',
                 {'article': article,
                  'author': author,
                  'comment': comment
                  }
                 )


def about_author(request):
    return render(request, 'news_blog/about.html')

def new_article(request):
   if request.method == "POST":
       form = ArticleForm(request.POST)
       if form.is_valid():
           article = form.save(commit=False)
           article.published_date = timezone.now()
           article.save()
           return redirect('article', article_id=article.pk)
   else:
       form = ArticleForm()
   return render(request, 'news_blog/edit_article.html', {'form': form})


def edit_article(request, article_id):
   article = get_object_or_404(Article, pk=article_id)
   if request.method == "POST":
       form = ArticleForm(request.POST, instance=article)
       if form.is_valid():
           article = form.save(commit=False)
           article.published_date = timezone.now()
           article.save()
           return redirect('article', article_id=article.pk)
   else:
       form = ArticleForm(instance=article)
   return render(request, 'news_blog/edit_article.html', {'form': form})


