from django.urls import path
from . import views


urlpatterns = [
    path('douban', views.movies_short, name='movies_short'),
    path('douban/select_short', views.select_short, name='select_short'),
    path('login1', views.login1, name='login1')
]
