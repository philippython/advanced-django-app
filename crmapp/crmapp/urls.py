from django.conf.urls import include, url
from django.contrib import admin
from marketing.views import Homepage

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Homepage.as_view(), name='home'),
]
