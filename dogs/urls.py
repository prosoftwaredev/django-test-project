from django.conf.urls import patterns, url

from dogs import views

urlpatterns = patterns('',
  url(r'^$', views.dogsList.as_view(), name='dogs_list'),
  url(r'^new$', views.dogsCreate.as_view(), name='dogs_new'),
  url(r'^edit/(?P<pk>\d+)$', views.dogsUpdate.as_view(), name='dogs_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.dogsDelete.as_view(), name='dogs_delete'),
)