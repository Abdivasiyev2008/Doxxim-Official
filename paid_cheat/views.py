from django.shortcuts import render
from .models import *
from django.views.generic import *
from hitcount.views import HitCountDetailView


# Create your views here.

def paidPubgCheatList(request):
    if 'q' in request.GET:
        q = request.GET['q']
        paid_cheat = PaidPubgCheat.objects.filter(about__icontains=q)

    else:
        paid_cheat = PaidPubgCheat.objects.all()

    context = {
        'paid_cheat': paid_cheat,
    }

    return render(request, 'paid_cheats/list.html', context)

class PaidPubgCheatDetailView(HitCountDetailView):
    model = PaidPubgCheat
    template_name = 'paid_cheats/detail.html'
    count_hit = True