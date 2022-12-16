from django.shortcuts import render, redirect
from django.http import HttpResponse

from blog.templates.forms import CommentForm
from .models import Mypost, Comment
# from blog.templates.myform import CustomForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contacts.html")


def mypost(request):
    # fetch all the data from the database
    mypost = Mypost.objects.all()

    # render the templates
    return render(request, "mypost.html", {"mypost": mypost})


def comments(request):
    comments = Comment.objects.all()

    return render(request, 'comments.html', {'comments': comments})


def main(request, slug):

    form = CommentForm()
    post = Mypost.objects.get(slug=slug)
    comment = Comment.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('main', slug=post.slug)

    else:
        form = CommentForm()

    context = {'form': form, 'post': post, 'comment': comment}

    return render(request, "main.html", context)
