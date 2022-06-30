from wsgiref.util import request_uri
from django.shortcuts import render
from jobsapp.models import ChennaiJobs, HydJobs, BangloreJobs

# Create your views here.
def homepage_view(request):
   return render(request, 'jobsapp/index.html')

def chennaijobs_view(request):
   jobs_list=ChennaiJobs.objects.all()
   my_dict={'jobs_list': jobs_list}
   return render(request, 'jobsapp/chennaijobs.html', context=my_dict)