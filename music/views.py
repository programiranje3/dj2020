from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def index(request):
#     return HttpResponse('<h1>John Lennon</h1>')
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from music.models import Band, Musician

context_footer = {
    'john': 'John Lennon',
    'life_quote': 'Life is what happens to you while you\'re busy making other plans.'
}


def index(request):
    # return HttpResponse('<h1>John Lennon</h1>')
    context = {
        'john': 'John Lennon',
        'life_quote': 'Life is what happens to you while you\'re busy making other plans.'
    }
    return render(request, 'index.html', context=context)


class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # context = {
        #     'john': 'John Lennon',
        #     'life_quote': 'Life is what happens to you while you\'re busy making other plans.'
        # }
        return render(request, 'index.html', context=context_footer)


class BandListView(ListView):

    model = Band
    template_name = 'music/band-list.html'

    def get_queryset(self):
        return Band.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class BandDetailView(DetailView):

    model = Band
    template_name = 'music/band-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class BandCreateView(CreateView):

    model = Band
    template_name = 'music/band-form.html'
    fields = '__all__'  # fields = ['name', 'country']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class BandUpdateView(UpdateView):

    model = Band
    template_name = 'music/band-form.html'
    fields = '__all__'  # fields = ['name', 'country']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class BandDeleteView(DeleteView):

    model = Band
    template_name = 'music/band-confirm-delete.html'
    success_url = reverse_lazy('band-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class MusicianListView(ListView):

    model = Musician
    template_name = 'music/musician-list.html'

    def get_queryset(self):
        return Musician.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class MusicianDetailView(DetailView):

    model = Musician
    template_name = 'music/musician-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class MusicianCreateView(CreateView):

    model = Musician
    template_name = 'music/musician-form.html'
    fields = '__all__'  # fields = ['name', 'country']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class MusicianUpdateView(UpdateView):

    model = Musician
    template_name = 'music/musician-form.html'
    fields = '__all__'  # fields = ['name', 'country']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context


class MusicianDeleteView(DeleteView):

    model = Musician
    template_name = 'music/musician-confirm-delete.html'
    success_url = reverse_lazy('musician-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(context_footer)
        return context





