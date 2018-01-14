from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^runs/add$', login_required(run_add_view), name="run_add_url"),
    url(r'^runs$', login_required(RunView.as_view()), name="runs_url"),
    url(r'^runs1$', login_required(RunView1.as_view()), name="runs1_url"),

    url(r'^horses/$', login_required(horse), name="horse_url"),


    # url(r'^run', login_required(run_view), name="run_url"),
    # url(r'^base', login_required(view1)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)