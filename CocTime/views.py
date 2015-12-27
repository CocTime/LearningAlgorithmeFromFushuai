from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'CocTime/index.html'
    level = 15
    context_object_name = ['test', 'tt']

    def get_queryset(self):
        return {

        }


def index(request):
    context = {'test': [1, 2, 3]}
    return render(request, 'CocTime/index.html', context)

