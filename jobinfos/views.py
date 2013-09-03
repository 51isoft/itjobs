from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from jobinfos.models import JobInfo

def index(request):
  jobs_list = JobInfo.objects.order_by('-pub_date', '-id')
  return render(request, 'jobinfos/index.html', { 'jobs_list': jobs_list })

def detail(request, job_id):
  try:
    job = JobInfo.objects.get(id=job_id)
  except JobInfo.DoesNotExist:
    raise Http404
  return render(request, 'jobinfos/detail.html', {'job': job})
