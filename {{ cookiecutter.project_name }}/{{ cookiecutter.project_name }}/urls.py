# --coding: utf8--

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    '',

    url(r'^$', TemplateView.as_view(TemplateView='index.html'), name='index'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt',
                                              content_type='text/plain')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
