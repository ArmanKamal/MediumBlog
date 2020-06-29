from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import BlogPost
from .forms import ContactForm,BlogPostForm,BlogPostModelForm

    
def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    context = {'object_list': qs}
    return render(request,"blog/list.html",context) 

# @login_required(login_url='/login')
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)

    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        return redirect('/blog')
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

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None , instance=obj)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request, "blog/create.html", context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('/blog')
    return render(request, "blog/delete.html")



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request,"contact/contact.html",{"form":form})


def login_page(request):
    return render(request,"contact/login.html",{})