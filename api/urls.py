from django.urls import path

from api.views import *

urlpatterns = [
    path('moim/', MoimListView.as_view(), name='moim'),
]