from django.conf.urls import patterns, include, url
from django.contrib import admin
from treehouse import views

urlpatterns = patterns('',
    url(r'^books/$', views.books, name='books'),
    url(r'^book/(?P<object_id>\w+)/$', views.book, name='book'),
    url(r'^reflection/(?P<id>\w+)/$', views.reflection, name='reflection'),
    url(r'^action/(?P<id>\w+)/$', views.action, name='action'),
    url(r'^post/(?P<id>\w+)/$', views.post, name='post'),
)
