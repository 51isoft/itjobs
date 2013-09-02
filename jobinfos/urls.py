from django.conf.urls import patterns, url

from jobinfos import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<job_id>\d+)/$', views.detail, name='detail'),
)
