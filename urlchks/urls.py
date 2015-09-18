from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /urlchks/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # # ex: /urlchks/5/
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # # ex: /urlchks/5/results/
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),


]