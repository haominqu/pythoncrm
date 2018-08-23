from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^userlogin', UserLogin.as_view(), name='user_login'),
    url(r'^manager', Manager.as_view(), name='about_manager'),
    url(r'^center', Centers.as_view(), name='about_center'),
    url(r'^classes', ClassesAPI.as_view(), name='about_classes'),
    url(r'^classactive', ClassActive.as_view(), name='active_classes'),
    url(r'^edus', EduAPI.as_view(), name='edus_show'),

    # url(r'^test/', TemplateView.as_view(template_name="test.html"), name='test'),
]