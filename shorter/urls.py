from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('link_stat/<str:short_link>/', LinkStatView.as_view(), name='link_stat'),
    path('r/<str:short_link>/', LinkRedirectView.as_view(), name='link_redirect'),
    path('shorter/', LinkShorterView.as_view(), name='shorter'),
]