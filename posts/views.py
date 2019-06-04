from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse("Hello from post")

    pt = Post.objects.all()[:10]

    context = {
        'title':'Latest Posts',
        'posts':pt
    }

    return render(request,'posts/index.html', context)


def details(request, id):
    ps = Post.objects.get(id=id)

    context = {
        'post':ps
    }
     
    return render(request,'posts/details.html', context)