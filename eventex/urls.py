from django.urls import path
from django.contrib import admin

import eventex.core.views

from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    path('', eventex.core.views.home),
    path('inscricao/', subscribe),
    path('inscricao/<int:pk>/', detail),
    path('admin/', admin.site.urls),

]


