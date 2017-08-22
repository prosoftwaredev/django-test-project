from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dogs/', include('dogs.urls', namespace='dogs')),
    url(r'^cats/', include('cats.urls', namespace='cats')),
    url(r'^owners/', include('owners.urls', namespace='owners')),
    url(r'^$', 'cats.views.home'),
]
