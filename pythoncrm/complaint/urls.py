from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^pcomplaint/', ComplaintP.as_view(), name='complaint'),
    url(r'^mcomplaint/', ManagerComplaint.as_view(), name='mcomplaint'),
    url(r'^allcomplaint/', AllComplaint.as_view(), name='allcomplaint'),
    url(r'^teacherlist/', TeacherList.as_view(), name='teacherlist'),


]