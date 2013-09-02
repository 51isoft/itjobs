import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from jobinfos.models import JobInfo

class Command(BaseCommand):
  args = ''
  help = 'Update Job Infos'

  def handle(self, *args, **options):
    new_data = JobInfo(title='test', pub_date=timezone.now())
    new_data.save()
    self.stdout.write('Test')
