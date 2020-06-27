from django.shortcuts import render,get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import ContactForm,BlogPostForm,BlogPostModelForm

    
def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    context = {'object_list': qs}
    return render(request,"blog/list.html",context) 


def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)

    if form.is_valid():
        obj = form.save()
        form = BlogPostModelForm()
    context = {'form':form}
    return render(request,"blog/create.html",context) 


def blog_post_detail_view(request,slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 1:
            obj = queryset.first()
    else:
        raise Http404
    context = {'object':obj}
    return render(request,"blog/detail.html",context)


def blog_post_update_view(request):
    return 

def blog_post_delete_view(request):
    return 



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request,"contact/contact.html",{"form":form})