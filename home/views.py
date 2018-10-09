from django.shortcuts import render
from django.http import HttpResponse

from home.models import SyntaxPost

# Create your views here.
post = [
    {
        'author':'jane',
        'author2':'sosa',
    }
]
def home(request):
    sp =SyntaxPost.objects.all()
    #sp = SyntaxPost.objects.first()
    context = {
        'post':post,
        'post2':sp
    }
    return render(request,'home/home.html',context)

def about(request):
    return HttpResponse('<hi>Blog About</h1>')
