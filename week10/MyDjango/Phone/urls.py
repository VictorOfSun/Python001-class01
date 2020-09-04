from django.urls import path
from . import views


urlpatterns = [
    path('', views.phones_index, name='phones_index'),
    path('phone/<str:name>', views.phones_short, name='phones_short'),
    path('phone/select_short/<str:name>', views.select_short, name='select_short'),
    path('login1', views.login1, name='login1')
]
