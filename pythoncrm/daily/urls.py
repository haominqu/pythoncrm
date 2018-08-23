from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^dailydetail/', DailyDetail.as_view(), name='daily_detail'),
    url(r'^dailyedit/', DailyEdit.as_view(), name='daily_edit'),
    url(r'^dailyshow/', DailyShow.as_view(), name='daily_show'),
    url(r'^dailyny/', HarryNY.as_view(), name='daily_ny'),
    url(r'^excel/', HarryNY.as_view(), name='daily_excel'),
    url(r'^aboutleader/', Leader.as_view(), name='about_leader'),
    url(r'^sendemail/', SendEmail.as_view(), name='send_email'),

]