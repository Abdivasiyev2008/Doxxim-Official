from django.urls import *
from .views import *

urlpatterns = [
    path('', paidPubgCheatList, name='paid-cheat-list'),
    path('<int:pk>/', PaidPubgCheatDetailView.as_view(), name='paid-cheat-detail')
]