from django.urls import *
from .views import *

urlpatterns = [
    path('', freePubgCheatList, name='free-cheat-list'),
    path('<int:pk>/', FreePubgCheatDetailView.as_view(), name='free-cheat-detail')
]