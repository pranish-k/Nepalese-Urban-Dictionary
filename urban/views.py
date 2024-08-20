from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


def index(request):
    words = Word.objects.all()
    context = {'words': words}
    return render(request, 'urban/home.html', context)


def submit(request):
    form = WordForm()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'urban/submit.html', context)


def search(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            words = Word.objects.filter(title__icontains=query)
            context = {'words': words, 'query': query}
            return render(request, 'urban/search.html', context)
    context = {'form': form}
    return render(request, 'urban/search.html', context)


def define(request, word_slug):
    word_title = word_slug.replace('-', ' ')
    word = get_object_or_404(Word, title__iexact=word_title)
    context = {'word': word}
    return render(request, 'urban/define.html', context)
