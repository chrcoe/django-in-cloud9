import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
# attempt to get static files working ...
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
# from polls import settings
from c9_django_test import settings

admin.autodiscover()

urlpatterns = patterns('',
    # points to base index page (c9-django-test/views.py etc.)
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()