from django.urls import path
from django.contrib import admin

import eventex.core.views

from eventex.subscriptions.views import subscribe

urlpatterns = [
    path('', eventex.core.views.home),
    path('inscricao/', subscribe),
    path('admin/', admin.site.urls),

]


