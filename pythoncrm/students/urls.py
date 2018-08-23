from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^stulogin', StudLogin.as_view(), name='stu_login'),
    url(r'^stuedit', Student.as_view(), name='stu_edit'),
    url(r'^stuclass', StuClass.as_view(), name='stu_class'),
    url(r'^stustatus', StudStatus.as_view(), name='stu_status'),
    # url(r'^test/', TemplateView.as_view(template_name="test.html"), name='test'),
]