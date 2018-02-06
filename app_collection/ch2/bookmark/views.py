from django.shortcuts import render
from .models import Bookmark
from django.views.generic import ListView, DetailView

# Create your views here.


class BookmarkLV(ListView):
    "ListView"
    model = Bookmark

class BookmarkDV(DetailView):
    "DetailView"
    model = Bookmark