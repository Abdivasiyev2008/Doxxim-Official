from django.urls import *
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
