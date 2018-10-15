from django.shortcuts import render
from django.http import HttpResponse

from home.models import SyntaxPost,Language
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts =SyntaxPost.objects.all()
    languages = Language.objects.all()
    #sp = SyntaxPost.objects.first()
    context = {
        'posts':posts,
        'languages':languages,
    }
    return render(request,'home/home.html',context)

def syntaxposts(request):
    posts =SyntaxPost.objects.all()
    languages = Language.objects.all()
    #sp = SyntaxPost.objects.first()
    context = {
        'posts':posts,
        'languages':languages,
    }
    return render(request,'home/syntaxposts.html',context)

@login_required
def favorites(request):

    return render(request,'home/favorites.html',None)

#def about(request):
#    return HttpResponse('<hi> About</h1>')
