from datetime import datetime

from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
    
    # class Meta:
    #     verbose_name_plural = 'posts', this is to define how the model name in plural should be!

