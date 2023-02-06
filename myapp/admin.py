from django.contrib import admin
from myapp.models import datagithub,imgcertificate


class datagithubAdmin(admin.ModelAdmin):
    list_display=['id','name_project','title_project','Url_project']  #สร้างตาราง
class dimgcertificateAdmin(admin.ModelAdmin):
    list_display=['id','certificate_img']  #สร้างตาราง


admin.site.register(datagithub,datagithubAdmin)
admin.site.register(imgcertificate,dimgcertificateAdmin)
