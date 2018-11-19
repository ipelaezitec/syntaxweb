from django.shortcuts import render,redirect
from django.http import HttpResponse

from home.models import SyntaxPost,Language,Marker,Sentence,Report
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

#temporal
def syntaxposts(request):
    print(request.GET)
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
    usuario = request.user.id
    markers = Marker.objects.filter(user=usuario)
    print(markers)

    context = {
        'usuario':usuario,
        'markers':markers,
    }
    return render(request,'home/favorites.html',context)


######################################## PANEL

@staff_member_required
def panel(request):
    usuario = request.user.id

    context = {}
    return render(request,'home/panel/panel.html',context)

@staff_member_required
def langpulls(request):
    # esta para el orto, pero me cansé de renegar con esta query
    langpulls = Language.objects.filter(active=False).order_by('-created')

    context = {
        'langpulls':langpulls,
    }
    return render(request, 'home/panel/langpulls.html',context)

@staff_member_required
def langpull(request,id):
    syntaxposts = SyntaxPost.objects.filter(language_id=id)
    #languageName = syntaxposts.first().language
    #print(languageName)

    context={
        'syntaxposts': syntaxposts,

    }
    return render(request,'home/panel/langpull.html',context)

@staff_member_required
def updateLanguage(request,id):
    lang = Language.objects.get(id=id)

    lang.active = True
    lang.save()
    return redirect('langpulls')

@staff_member_required
def languages(request):
    langs = Language.objects.filter(active=True).order_by('-created')
    context = {
        'langs':langs,
    }
    return render(request, 'home/panel/langs.html',context)

@staff_member_required
def lang(request,id):
    syntaxposts = SyntaxPost.objects.filter(language_id=id)

    context={
        'syntaxposts': syntaxposts,

    }
    return render(request,'home/panel/lang.html',context)

@staff_member_required
def reports(request):
    reports = Report.objects.filter(resolved='N').order_by('-created')
    print (reports)
    context = {
        'reports': reports,
    }
    return render(request, 'home/panel/reports.html', context)

@staff_member_required
def report (request,id):
    report = Report.objects.get(pk=id)
    print (report)

    context = {
        'report':report,
    }
    return render(request, 'home/panel/report.html', context)