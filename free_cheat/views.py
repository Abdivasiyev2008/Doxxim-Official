from django.shortcuts import render
from .models import *
from django.views.generic import *
from hitcount.models import HitCount
from hitcount.views import HitCountMixin, HitCountDetailView
from .forms import *

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

    def post(self, request, *args, **kwargs):
        new_comment = CommentBlog(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(FreePubgCheatDetailView, self).get_context_data(*args, **kwargs)
        data = super().get_context_data(**kwargs)

        comments_connected = CommentBlog.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance = self.request.user)
        
        context.update(data)
        return context