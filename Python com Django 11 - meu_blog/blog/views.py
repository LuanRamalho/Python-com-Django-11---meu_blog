from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Message
from .forms import PostForm, MessageForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    messages = post.messages.all()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.post = post
            message.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = MessageForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'messages': messages, 'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})