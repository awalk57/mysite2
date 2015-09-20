from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, request
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Applications, Urls, ListUrlFilter

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'urlchks/index.html'
    context_object_name = 'Agency_list'

    def get_queryset(self):
        """
        Return the first five agencies.
        """
        return Applications.objects.order_by('agency')[:5]

    def url_list(self):
        f= ListUrlFilter(request.GET, queryset=Urls.objects.all())
        return render_to_response('urlchks/template.html',{'filter': f})


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'urlchks/detail.html'
#

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'urlchks/results.html'



