from django.contrib import admin
from jobsapp.models import ChennaiJobs, HydJobs, BangloreJobs

# Register your models here.
class ChennaiJobsAdmin(admin.ModelAdmin):
   list_display=['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

admin.site.register(ChennaiJobs, ChennaiJobsAdmin)

class HydJobsAdmin(admin.ModelAdmin):
   list_display=['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

admin.site.register(HydJobs, HydJobsAdmin)

class BangloreJobsAdmin(admin.ModelAdmin):
   list_display=['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

admin.site.register(BangloreJobs, BangloreJobsAdmin)