from django.contrib import admin

# Register your models here.
from .models import Coworker, News, Colleges, Library_fund, Rooms, Library_services, Exhibitions 

admin.site.register(News)
admin.site.register(Colleges)
admin.site.register(Coworker)
admin.site.register(Library_fund)
admin.site.register(Rooms)
admin.site.register(Library_services)
admin.site.register(Exhibitions)


#super user admin pass:admin1     admin@ukr.net