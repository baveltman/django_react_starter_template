from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions/', views.questions_static, name='questions_static'),
    url(r'^react/questions/', views.questions_react, name='questions_static')
]