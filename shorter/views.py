from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404, redirect

from .models import Link
from .forms import LinkForm
from django.shortcuts import redirect

class IndexView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'shorter/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = True
        return context

class LinkShorterView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'shorter/link_shorter.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = True
        return context
    
    
class LinkStatView(DetailView):
    model = Link
    template_name = 'shorter/link_stat.html'
    
    def get_object(self):
        return get_object_or_404(Link, short_link=self.kwargs['short_link'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        link = self.object
        context['short_link'] = link.short_link
        context['index'] = False
        link.short_link = settings.MY_SITE_DOMAIN +'r/'+ link.short_link
        # context['short_link'] = link.short_link.replace('http://127.0.0.1:8000/redirect/', '')
        context['link'] = link
        return context


class LinkRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, short_link=self.kwargs['short_link'])
        link.count += 1
        link.save()
        return link.url