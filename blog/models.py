from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title