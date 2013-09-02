from django.shortcuts import render
from django.http import HttpResponse

from jobinfos.models import JobInfo

def index(request):
  return render(request, 'jobinfos/index.html')
