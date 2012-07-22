from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'bank.views.index', name='index'),
	url(r'^account/(\d+)/$', 'bank.views.account', name='account'),
	url(r'^account/(\d+)/addnote/$', 'bank.views.addnote', name='addnote'),
	url(r'^account/(\d+)/note/(\d+)/delnote/$', 'bank.views.delnote', name='delnote'),
	url(r'^account/addaccount/$', 'bank.views.addaccount', name='addaccount'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'bank/login.html'}),
	url(r'^accounts/login/registration/$', 'client.views.registration', name='registration'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'bank/logout.html'}),
	url(r'^accounts/addcategory/$', 'bank.views.addcategory', name = 'category-add'),
    # Examples:
    # url(r'^$', 'money.views.home', name='home'),
    # url(r'^money/', include('money.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()