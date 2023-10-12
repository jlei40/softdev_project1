from django.shortcuts import render
from .Character_forms import CharacterForm
from django.shortcuts import render, redirect
from django.contrib import messages

import datetime
import json



# Create your views here.

def index(request):
    title_page = 'Characters Index'
    return render(request, 'Characters/index.html',
        context = {'title_page' : title_page,
                    })
    
def cookies(request):
   dico_cookies = request.COOKIES
   visit_nbr = 0
   if 'visit_nbr' in dico_cookies:
       try:
           visit_nbr = int(dico_cookies['visit_nbr']) + 1
       except:
           visit_nbr = 1
   else:
       visit_nbr = 1
   response = render(request, "Characters/cookies.html",
                     context={'visit_nbr': visit_nbr})
   response.set_cookie(key="visit_nbr", value=visit_nbr,expires=datetime.datetime(2024, 10, 2, 18, 23))
   return response

def character_info(request):
    dico_cookies = request.COOKIES
    dico_context = {}
    if 'character_data' in dico_cookies:
        try:
            dico_character_data = json.loads(dico_cookies['character_data'])
            dico_context['character_data'] = dico_character_data
        except:
            messages.add_message(request, messages.ERROR, "There is an error on your character data")
    return render(request, "Characters/character_info.html", context=dico_context)

def djangoforms(request):
    if request.method == "POST":
        if 'character_name' not in request.POST or 'character_year' not in request.POST:
            messages.add_message(request, messages.ERROR, "The form sent is incomplete")
            return render(request, "Characters/forms.html")

        response = redirect('Characters:character_info')
        response.set_cookie(key="character_data", value=json.dumps(
            {'character_name': request.POST['character_name'],
            'character_year': request.POST['character_year']}))
        return response
    return render(request, "Characters/djangoforms.html")


def nondjangoforms(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
        # process the data
            response = redirect('Characters:character_info')
            print("name", form.cleaned_data['name'])
            print("characters", form.cleaned_data['Characters'])
            print("year", form.cleaned_data['year'])
            response.set_cookie(key="character_data", value=json.dumps(
            {'character_name': request.POST['name'],
            'characters': request.POST['Characters'],
            'character_year': request.POST['year']}))


        return response
    else:
        form = CharacterForm()
    return render(request, "Characters/nondjangoforms.html", {'character_form': form})


