from django.db import models

# Create your models here.
class JsonField(models.TextField):
    pass


class Host(models.Model):
    href = models.URLField()
    cluster_name = models.CharField(max_length='100', default='')
    cpu = models.CharField(max_length='100')
