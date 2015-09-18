from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Applications, Urls

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'urlchks/index.html'
    context_object_name = 'Agency_list'

    def get_queryset(self):
        """
        Return the first five agencies.
        """
        return Applications.objects.order_by('agency')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'urlchks/detail.html'
#

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'urlchks/results.html'

