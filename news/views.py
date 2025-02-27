from django.shortcuts import render
from .models import NewsArticle, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import NewsArticle, Favourite
from .models import NewsArticle

def home(request):
    news_articles = NewsArticle.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'home.html', {'news_articles': news_articles, 'categories': categories})

def category_news(request, category_id):
    category = Category.objects.get(id=category_id)
    news_articles = NewsArticle.objects.filter(category=category).order_by('-created_at')
    return render(request, 'category_news.html', {'news_articles': news_articles, 'category': category})


@login_required
def add_favourite(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    Favourite.objects.get_or_create(user=request.user, article=article)
    return redirect('favourite_articles')

@login_required
def remove_favourite(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    Favourite.objects.filter(user=request.user, article=article).delete()
    return redirect('favourite_articles')

@login_required
def favourite_articles(request):
    favourites = Favourite.objects.filter(user=request.user).select_related('article')
    return render(request, 'favourites.html', {'favourites': favourites})

def news_detail(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(user=request.user, article=article).exists()
    return render(request, 'news_detail.html', {'article': article, 'is_favourite': is_favourite})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})