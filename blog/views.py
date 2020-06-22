from django.shortcuts import render

# Create your views here.
from .models import BlogPost



def blog_post_detail_page(request, post_id):
    obj = BlogPost.objects.get(id=post_id)
    context = {'object':obj}
    return render(request,"blog/blog_post_detail.html",context)