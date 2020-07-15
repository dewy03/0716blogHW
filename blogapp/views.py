from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import BlogFrame

# Create your views here.
def main(request):
    blog = BlogFrame.objects.all().order_by('-id')
    return render(request, 'main.html', {'blog':blog})

def detail(request, blog_id):
    blogdetail = get_object_or_404(BlogFrame, pk=blog_id)
    return render(request, 'detail.html', {'blogdetail':blogdetail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = BlogFrame()
    blog.title = request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()
    return redirect('/detail/' + str(blog.id))

def renew(request, blog_id):
    blog = get_object_or_404(BlogFrame, pk=blog_id)
    return render(request, 'renew.html', {'blog':blog})

def delete(request, blog_id):
    blog = get_object_or_404(BlogFrame, pk=blog_id)
    blog.delete()
    return redirect('main')

def update(request, blog_id):
    blog = get_object_or_404(BlogFrame, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))
