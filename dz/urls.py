from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mainapp.urls')),
    url(r'^', include('authorisation.urls')),
]
