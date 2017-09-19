from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Bookmark
# Create your views here.

class BookmarkListV(ListView):
    model = Bookmark

class BookmarkDetailV(DetailView):
    model = Bookmark

class BookmarkCreateV(CreateView):
    model = Bookmark
    fields = ['title', "url"]

class BookmarkUpdateV(UpdateView):
    model = Bookmark
    fields = ['title', "url"]
