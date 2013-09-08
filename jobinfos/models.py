from django.db import models

class JobInfo(models.Model):
  title = models.CharField(max_length = 2048)
  content = models.TextField()
  pub_date = models.DateField()
  url = models.CharField(max_length = 1024)
  source = models.CharField(max_length = 1024)

class ExpInfo(models.Model):
  title = models.CharField(max_length = 2048)
  content = models.TextField()
  pub_date = models.DateField()
  url = models.CharField(max_length = 1024)
  source = models.CharField(max_length = 1024)
