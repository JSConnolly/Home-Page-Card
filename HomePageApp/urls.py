from django.conf.urls import *
from HomePageApp.views import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
						url(r'^$', 'HomePageApp.views.home_page', name='home_page'),
						url(r'^projects/$', 'HomePageApp.views.projects_page', name='projects_page'),
						url(r'^learn/$', 'HomePageApp.views.learning_page', name='learning_page'),
    # Examples:
    # url(r'^$', 'HomePageApp.views.home', name='home'),
    # url(r'^HomePageApp/', include('HomePageApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
                        (r'^HomePageApp/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
