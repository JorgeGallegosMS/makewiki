from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """Shows a list of all wiki pages"""
    model = Page

    def get(self, request):
        """ Returns a list of wiki pages."""
        wikis = Page.objects.all()
        context = {
          'wikis': wikis
        }
        return render(request, 'wiki/list.html', context)


class PageDetailView(DetailView):
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        wiki = Page.objects.get(slug=slug)
        context = {
          'wiki': wiki
        }
        return render(request, 'wiki/page.html', context)

    def post(self, request, slug):
        pass
