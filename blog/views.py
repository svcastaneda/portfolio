from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def posts(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/all_posts.html', {'posts': posts})
    
def content(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})
    