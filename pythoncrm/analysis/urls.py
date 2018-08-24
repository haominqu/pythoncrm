from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^indexanalysis/', IndexAnalysis.as_view(), name='index_analysis'),

    # url(r'^test/', TemplateView.as_view(template_name="test.html"), name='test'),
]