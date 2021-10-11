from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'webpage3/post_list.html')

