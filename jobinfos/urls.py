from django.conf.urls import patterns, url

from jobinfos import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<page>\d+)/$', views.index, name='index_page'),
  url(r'^joblist/$', views.joblist, name='joblist'),
  url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
  url(r'^explist$', views.explist, name='explist'),
  url(r'^exp/(?P<exp_id>\d+)/$', views.expdetail, name='expdetail'),
  url(r'^youdaonote/', views.youdaonote, name='youdaonote'),
)
