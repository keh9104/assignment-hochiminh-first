from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "contents",
            "price",
            "rating",
            "img",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content": (""),
        }
        widgets = {
            "content": forms.Textarea(attrs={"placeholder": "댓글을 입력하세요"}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
        )
        # labels = {
        #     "email": (""),
        #     "first_name": (""),
        #     "last_name": (""),
        #     "username": (""),
        #     "password": (""),
        # }
        widgets = {
            "email": forms.TextInput(attrs={"placeholder": "email"}),
            "first_name": forms.TextInput(attrs={"placeholder": "first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "last name"}),
            "username": forms.TextInput(attrs={"placeholder": "user ID"}),
            "password": forms.PasswordInput(attrs={"placeholder": "password"}),
        }
