#!python3

from django.shortcuts import render
from inicio.models import Post
from inicio.models import Projeto
from inicio.models import Exoplanetas
from inicio.models import Documentation
from inicio.models import ProgramasGit

# Create your views here.
def home(request): #recebe a solicitação do usuario
    posts= Post.objects.all()
    return render(request,'inicio.html',{'post': posts}) #devolve a pagina que quer ser mostrada


def post(request, post_id):
    post= Post.objects.get(pk=post_id)
    return render (request, 'post.html', {'post': post})

def sobre_o_projeto (request):
    proj= Projeto.objects.all()
    return render(request, 'projeto.html',{'proj': proj})

def exoplanetas(request):
    exoplanetas= Exoplanetas.objects.all()
    return render(request, 'exoplanetas.html',{'exoplanetas': exoplanetas})

def documentation(request):
    doc= Documentation.objects.all()
    return render(request, 'documentacao.html',{'doc': doc})

def livro(request):
    return render(request,'livro.html')


def programasgit(request):
    pgr_git= ProgramasGit.objects.all()
    return render(request, 'programas-git.html',{'pgr_git': pgr_git})

    


