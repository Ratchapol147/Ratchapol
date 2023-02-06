from django.db import models


class datagithub (models.Model):
    name_project = models.CharField(max_length=100)
    title_project = models.TextField()
    Url_project = models.CharField(max_length=100)

class imgcertificate (models.Model):
    certificate_img = models.ImageField(upload_to='images',blank=True)