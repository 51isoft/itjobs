# coding=UTF-8

import datetime
import urllib
import urllib2
import re

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from jobinfos.models import JobInfo

from bs4 import BeautifulSoup

class Dajie:
  def CrawlDetail(self, url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    return str(soup.find_all("div", class_="jd-mode")[0])

  def CrawlJobs(self, page):
    url = "http://s.dajie.com/projects/all-jisuanji-all/" + str(page)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    for link in soup.find_all("a"):
      url = str(link.get('href'))
      if re.match(r'^/projects/.*\.html$', url):
        print "Processing " + url
        try:
          job = JobInfo.objects.get(title=link.get_text())
        except JobInfo.DoesNotExist:
          job = JobInfo()
          job.title = link.get_text()
        job.url = "http://s.dajie.com" + url
        job.pub_date = str(datetime.datetime.now().year) + "-" + link.parent.find_next_sibling().get_text()
        job.content = self.CrawlDetail(job.url)
        job.save()

  def CrawlIndexPage(self):
    concerned = [u'电气工程', u'信息工程', u'网络工程', u'电子商务']
    url = "http://s.dajie.com/2014"
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    for link in soup.find("div", class_="item-1").find_all("a"):
      url = str(link.get('href'))
      if re.match(r'^/projects/.*\.html$', url):
        subjects = link.parent.find_next_sibling().find_next_sibling().find_next_sibling()
        if len(set(subjects.get_text().split()).intersection(set(concerned))) > 0:
          print "Processing " + url
          try:
            job = JobInfo.objects.get(title=link.get_text())
          except JobInfo.DoesNotExist:
            job = JobInfo()
            job.title = link.get_text()
          job.url = "http://s.dajie.com" + url
          job.pub_date = str(datetime.datetime.now().year) + "-" + link.parent.find_next_sibling().get_text()
          job.content = self.CrawlDetail(job.url)
          job.save()


class NewSmth:
  def CrawlDetail(self, url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    return str(soup.find_all("td", class_="a-content")[0])

  def CrawlJobs(self, page):
    url = "http://www.newsmth.net/nForum/board/Career_Campus?ajax&p=" + str(page)
    html = urllib2.urlopen(url).read().decode('GBK')
    soup = BeautifulSoup(html, "lxml")
    for row in soup.find('table').find('tbody').find_all('tr'):
      if row.get('class') is None:
        link = row.find_all('a')[1]
        url = str(link.get('href'))
        pub_text = row.find_all('td')[2].get_text()

        print "Processing " + url
        try:
          job = JobInfo.objects.get(title=link.get_text())
        except JobInfo.DoesNotExist:
          job = JobInfo()
          job.title = link.get_text()
        job.url = "http://www.newsmth.net" + url + "?ajax"
        if pub_text.find(':') == -1:
          job.pub_date = pub_text
        else:
          job.pub_date = datetime.datetime.now()
        job.content = self.CrawlDetail(job.url)
        job.save()


class CareerBNU:
  def CrawlDetail(self, url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    return str(soup.find("dl").find("dd"))

  def CrawlJobs(self, page):
    url = "http://career.bnu.edu.cn/JobInfomation.aspx?catid=470"
    data = {}
    values = {'__EVENTTARGET' : 'AspNetPager1',
          '__EVENTARGUMENT' : str(page) }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, "lxml")
    for row in soup.find('dl', class_='ji120101').find_all('dd'):
      link = row.find_all('a')[0]
      url = str(link.get('href'))
      pub_text = row.find_all('td')[1].get_text().strip()

      print "Processing " + url
      try:
        job = JobInfo.objects.get(title=link.get_text())
      except JobInfo.DoesNotExist:
        job = JobInfo()
        job.title = link.get_text()
      job.url = "http://career.bnu.edu.cn/" + url
      job.pub_date = pub_text
      job.content = self.CrawlDetail(job.url)
      job.save()


class Command(BaseCommand):
  args = ''
  help = 'Update Job Infos'
  option_list = BaseCommand.option_list + (
    make_option('--init',
      action='store_true',
      dest='init',
      default=False,
      help='First time crawl'),
    )

  def handle(self, *args, **options):
    smth = NewSmth()
    dajie = Dajie()
    bnu = CareerBNU()
    if options['init']:
      dajie.CrawlIndexPage()
      for i in range(1,10):
        dajie.CrawlJobs(i)
        smth.CrawlJobs(i)
        bnu.CrawlJobs(i)
    else:
      dajie.CrawlIndexPage()
      dajie.CrawlJobs(1)
      smth.CrawlJobs(1)
      bnu.CrawlJobs(1)
