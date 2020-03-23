from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.get_username()
            post.save()
            return redirect("detail", post.pk)
    else:
        form = PostForm()
    return render(request, "new.html", {"form": form})


def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.get_username()
            comment.post = post
            comment.save()
        return redirect("detail", post.pk)
    else:
        form = CommentForm()
    return render(request, "detail.html", {"post": post, "form": form})


@login_required
def edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect("detail", post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "edit.html", {"form": form})


@login_required
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect("home")


@login_required
def delete_com(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect("detail", post_pk)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
        return redirect("home")
    else:
        form = UserForm()
    return render(request, "registration/signup.html", {"form": form})
