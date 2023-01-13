from django.shortcuts import render
from .models import *
from django.views.generic import *
from hitcount.models import HitCount
from hitcount.views import HitCountMixin, HitCountDetailView

# Create your views here.

def freePubgCheatList(request):
    if 'q' in request.GET:
        q = request.GET['q']
        free_cheat = FreePubgCheat.objects.filter(about__icontains=q)

    else:
        free_cheat = FreePubgCheat.objects.all()

    context = {
        'free_cheat': free_cheat,
    }

    return render(request, 'free_cheats/list.html', context)

class FreePubgCheatDetailView(HitCountDetailView):
    model = FreePubgCheat
    template_name = 'free_cheats/detail.html'
    count_hit = True