from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import Http404
from .models import post
from .forms import CommentForm





def base(request):
    return render(request,'base.html')

def frontpage(request):
    posts = post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_details(request, posted):
    try:
        post1 = post.objects.get(slug=posted)

    except post.DoesNotExist:
        raise Http404("Post does not exist")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post1 = post1
            comment.user=request.user
            comment.save()
        return redirect('post_details',posted=post1.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_details.html', {'post1': post1, 'form': form})


#def log_out(request):
    logout(request)
    return redirect('login')

 
