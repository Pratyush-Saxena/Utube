from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class video(models.Model):
    id = models.CharField(primary_key=True,max_length=100,editable=False)
    title = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail = models.CharField(max_length=250)
    publishedAt = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    tags = ListCharField(
        base_field=models.CharField(max_length=25),
        size=100,
        max_length=2600  # 6 * 10 character nominals, plus commas
    )
    def __str__(self):
        return self.id
  