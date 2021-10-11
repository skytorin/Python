from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    path('', views.post_list, name='post_list'),

]