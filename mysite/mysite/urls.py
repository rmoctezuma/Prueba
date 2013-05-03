from django.conf.urls import patterns, include, url
from mysite.views import hello, hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	('^hello/$', hello),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
