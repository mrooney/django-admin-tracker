from coffin.conf.urls.defaults import *
from django.contrib import admin
from django.shortcuts import redirect

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', lambda request: redirect('/admin/tasktrack/task')),
)
