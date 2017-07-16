
from django.conf.urls import url, include
from django.contrib import admin
from core import views as core_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^projects/$', core_views.projects, name='projects'),
    url(r'^wallets/$', core_views.wallets, name='wallets'),
    url(r'^hackers/$', core_views.hackers_list, name='hackers_list'),
    url(r'^checkin/$', core_views.checkin, name='checkin'),
    url(r'^login/$', core_views.user_login, name='login'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^judges/$', core_views.home, name='home'),
    url(r'^investors/$', core_views.home, name='home'),
    url(r'/admin/oauth/', include('oauthadmin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
