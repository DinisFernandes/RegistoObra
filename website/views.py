
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic import TemplateView
from django.db.models import Q, Count, Case, When
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator



class PostList(ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.order_by('-data_post')
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['items'] = Post.objects.all().count()
        return context


class PostDetail(DetailView):
    model = Post

class PostBusca(PostList):
    num = 0
    template_name = 'website/post_busca.html'

    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo') or self.request.session['termo']
        qs = super().get_queryset(*args, **kwargs)
        if not termo:
            return qs

        self.request.session['termo'] = termo

        qs = qs.filter(
            Q(title__icontains=termo) |
            Q(content__icontains=termo)
        )
        self.request.session.save()
        return qs


class MapaBarroselas(TemplateView):
    template_name = 'website/map_barroselas.html'

class MapaChafe(TemplateView):
    template_name = 'website/map_chafe.html'

class MapaDarque(TemplateView):
    template_name = 'website/map_darque.html'

class MapaPortuzelo(TemplateView):
    template_name = 'website/map_portuzelo.html'

class MapaPerre(TemplateView):
    template_name = 'website/map_perre.html'

class MapaEspregueira(TemplateView):
    template_name = 'website/map_espregueira.html'

class MapaUrsulinas(TemplateView):
    template_name = 'website/map_ursulinas.html'

class MapaCardielos(TemplateView):
    template_name = 'website/map_cardielos.html'

class MapaFincao(TemplateView):
    template_name = 'website/map_fincao.html'

class MapaPortela(TemplateView):
    template_name = 'website/map_portela.html'