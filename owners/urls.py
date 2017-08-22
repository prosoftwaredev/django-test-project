from django.conf.urls import patterns, url

from owners import views

urlpatterns = patterns('',
  url(r'^$', views.owners_list, name='owners_list'),
  url(r'^new$', views.owners_create, name='owners_new'),
  url(r'^edit/(?P<pk>\d+)$', views.owners_update, name='owners_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.owners_delete, name='owners_delete'),
)