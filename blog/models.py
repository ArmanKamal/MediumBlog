from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL 



class BLogPostQueryset(models.QuerySet):
     def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BLogPostQueryset(self.model,using=self._db)
    def published(self):
        return self.get_queryset().published()


class BlogPost(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True,blank=True)
    timestamp =  models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)

    objects = BlogPostManager()
    class Meta:
        ordering = ['-publish_date','-update','-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"
    def get_delete_url(self):
            return f"/blog/{self.slug}/delete"
