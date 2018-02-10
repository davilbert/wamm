from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news_blog.urls')),
    path('about/', include('news_blog.urls'))
]
