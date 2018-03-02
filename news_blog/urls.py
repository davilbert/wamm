from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name='article'),
    path('about/', views.about_author, name='author'),
    path('new/', views.new_article, name='new_article'),
    path('<int:article_id>/edit', views.edit_article, name='edit'),
    path('past/',views.past_time, name='past'),
    path('now/', views.now_life, name='now'),
]


