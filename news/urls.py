from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/'), name='admin_logout'),
    path('favourite/add/<int:article_id>/', views.add_favourite, name='add_favourite'),
    path('favourite/remove/<int:article_id>/', views.remove_favourite, name='remove_favourite'),
    path('favourites/', views.favourite_articles, name='favourite_articles'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('news/<int:article_id>/', views.news_detail, name='news_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
