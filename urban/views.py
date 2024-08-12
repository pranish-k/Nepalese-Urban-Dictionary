from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index (request):
    words = Word.objects.all()
    context = {'words': words}
    return render(request, 'urban/home.html', context)

def submit(request):
    form = WordForm()
    if request.method =='POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'urban/submit.html',context)

def update(request, pk):
    word = Word.objects.get(id=pk)
    return render(request, 'urban/updatewords.html')