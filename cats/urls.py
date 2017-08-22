from django.conf.urls import patterns, url

from cats import views

urlpatterns = patterns('',
  url(r'^$', views.cats_list, name='cats_list'),
  url(r'^new$', views.cats_create, name='cats_new'),
  url(r'^edit/(?P<pk>\d+)$', views.cats_update, name='cats_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.cats_delete, name='cats_delete'),
)