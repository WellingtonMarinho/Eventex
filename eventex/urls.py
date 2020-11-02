from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from eventex.core.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('', home),
    path('admin/', admin.site.urls),
    #path('', home),
    #path('admin/', admin.site.urls),
]


