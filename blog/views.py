from django.shortcuts import render
from blog.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "blog/home.html", {'posts':posts})

def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post.html", {'post':post})
    
def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")