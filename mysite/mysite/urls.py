from django.conf.urls import patterns, include, url
from mysite.views import hello, hours_ahead, hello_user, operadores

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^page/$', hello_user),
	('^hello/$', hello),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^timsa/Operadores', operadores),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
