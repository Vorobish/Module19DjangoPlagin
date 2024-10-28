from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

k = 3


# Create your views here.
def index(request):
    global k
    if request.method == 'POST':
        k = request.POST.get('k')
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, k)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'k': k,
    }

    return render(request, 'index.html', context)
