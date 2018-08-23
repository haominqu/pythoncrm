from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^userinfo/', include('userinfo.urls')),
    url(r'^daily/', include('daily.urls')),
    url(r'^exercise/', include('exercise.urls')),
    url(r'^interview/', include('interview.urls')),
    url(r'^front/', include('front.urls')),
    url(r'^complaint/', include('complaint.urls')),
    url(r'^student/', include('students.urls')),
    url(r'^test/', TemplateView.as_view(template_name="test.html"), name='test'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)