from django.shortcuts import render

# Create your views here.

def index(request):
    title_page = 'Characters Index'
    return render(request, 'Characters/index.html',
        context = {'title_page' : title_page,
                    })