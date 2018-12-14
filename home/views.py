from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from home.models import SyntaxPost,Language,Marker,Sentence,Report,Contact,Suggestion
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SyntaxForm, SuggestionForm, ContactForm
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer

# Create your views here.

def home(request):
    sentences = Sentence.objects.all()
    posts =SyntaxPost.objects.all()
    languages = Language.objects.all()
    #sp = SyntaxPost.objects.first()

    context = {
        'posts':posts,
        'languages':languages,
        'sentences':sentences,
    }
    return render(request,'home/home.html',context)


class Suggest(CreateView):
    template_name = 'home/suggest.html'
    form_class = SuggestionForm
    sucess_url = reverse_lazy('syntaxpost')

class Contacts(CreateView):
    template_name = 'home/contact.html'
    form_class = ContactForm

class ContactList(ListView):
    template_name = 'home/panel/list-contact.html'
    model = Contact
    paginate_by = 4

class SuggestionsList(ListView):
    template_name = 'home/panel/list-suggestions.html'
    model = Suggestion
    paginate_by = 4

def filtrar(request):
    pass
#temporal para probar boludeces, syntaxposts se puede totalmente borrar o modificar , incluso eliminar syntaxpost.html
# Aunque syntaxpost.html tiene el estilo de un post.
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
    
    langpulls = Language.objects.filter(active=False).order_by('-created')

    context = {
        'langpulls':langpulls,
    }
    return render(request, 'home/panel/langpulls.html',context)


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
    language = Language.objects.get(pk=id)
    if language.active == 'N':
        texto = {
            'usuario': 'Sugerido por',
            'lenguaje' : 'Lenguaje sugerido : '
        }
    else :
        texto = {
            'usuario': 'Sugerido por',
            'lenguaje': 'Lenguaje : '
        }
    print (language.active)
    context={
        'language':language,
        'syntaxposts': syntaxposts,
        'texto':texto,
    }
    return render(request,'home/panel/lang.html',context)

@staff_member_required
def editSyntax(request,id):
    #synposts = SyntaxPost.objects.all(id=id)

    item = get_object_or_404(SyntaxPost, id=id)
    post = SyntaxPost.objects.get(pk=id)
    
    form = SyntaxForm(request.POST or None, instance=item)
    context = {
        'syntaxpost': item,
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('lang', id=post.language.id)

    return render(request, 'home/panel/editsyntax.html', context)

@staff_member_required
def reports(request):
    reports = Report.objects.filter(resolved='N').order_by('-created')
    
    context = {
        'reports': reports,
    }
    return render(request, 'home/panel/reports.html', context)

@staff_member_required
def report (request,id):
    report = Report.objects.get(pk=id)
    postid = report.post.id

    item = get_object_or_404(SyntaxPost, id=postid)
    form = SyntaxForm(request.POST or None, instance=item)
    context = {
        'report': report,
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('report', id=id)

    return render(request, 'home/panel/report.html', context)


@staff_member_required
def reportsResolved(request):
    reports = Report.objects.filter(resolved='Y').order_by('-created')
    
    context = {
        'reports': reports,
    }
    return render(request, 'home/panel/reportsresolved.html', context)

@staff_member_required
def changeToResolved(request,id):
    report = Report.objects.get(id=id)

    report.resolved = 'Y'
    report.save()
    return redirect('reports')

@staff_member_required
def deleteReport(request,id):
    report = Report.objects.get(id=id)
    report.delete()
    return redirect('reports')

@api_view(['POST'])
def filterPosts(request):
    if request.method == 'POST' :
        data = request.data #List of languagues in 'param' ['Python','C#']
        res = []
        for i in data['param']: 
            try:
                post = SyntaxPost.objects.filter(language_id=i)
                for j in post:
                    imagePath = str(j.language.img)
                    res.append({
                        'id': j.id,
                        'name': j.language.name,
                        'content': j.content,
                        'image': imagePath,
                        'sentence': j.sentence.name,
                    })
            except ObjectDoesNotExist:
                print('El id ingresado no existe')
            
        return Response(res)