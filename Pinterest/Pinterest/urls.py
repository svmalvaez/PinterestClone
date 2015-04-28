from django.conf.urls import patterns, include, url
from django.contrib import admin
from pictures import views as pviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Pinterest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', pviews.Pin.as_view(), name="pin-index")
)
