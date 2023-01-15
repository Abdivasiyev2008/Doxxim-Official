from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
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

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PaidPubgCheatDetailView, self).get_context_data(*args, **kwargs)
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance = self.request.user)
        
        context.update(data)
        return context