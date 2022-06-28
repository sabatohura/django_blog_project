import imp
from multiprocessing import context
from django.http import Http404
from django.shortcuts import render,redirect
from blogapp.forms import BlogForm
from blogapp.models import Blog
# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request,"blog.html", context)

def add_blog(request):
    form = BlogForm()
    context = {"form":form}

    if request.method == 'POST':
        blog_form=BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect("blogs")
        else:
            context={'form':blog_form}
            return render(request,'add_form.html',context)
    return redirect(request,'add_form.html',context)

def delete_blog(request,blog_id):
    try:
         blog=Blog.objects.filter(id = blog_id)
    except Blog.DoesNotExist:
        raise Http404("blog does not exist")
    return redirect(blog)

def edit_blog(request,blog_id):
    blog=Blog.objects.filter(id=blog_id)
    context = {'blog':blog}
    

