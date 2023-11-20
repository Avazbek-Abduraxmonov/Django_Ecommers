from django.shortcuts import render
from app.models import *
# Create your views here.
def home(request):
    aboutme = AboutMe.objects.all()
    context = {
        'About':aboutme
    }
    return render(request, 'base.html', context=context)

def post(request):
    context = {}
    context['post_add'] = Post.objects.all()
    return render(request, 'post.html', context)


def shop(request):
    images = Img.objects.all()
    context = {
        'img':images
    }
    return render(request, 'shop.html', context=context)