from django.shortcuts import render
from .Character_forms import CharacterForm
from django.shortcuts import render, redirect
from django.contrib import messages

import datetime
import json
character_list = [{
    'Mario': {'name': 'Mario', 'image': ''},
    'Donkey Kong': {'name': 'Donkey Kong', 'image': ''},
    'Link': {'name': 'Link', 'image': ''},
    'Samus': {'name': 'Samus', 'image': ''},
    'Dark Samus': {'name': 'Dark Samus', 'image': ''},
    'Yoshi': {'name': 'Yoshi', 'image': ''},
    'Kirby': {'name': 'Kirby', 'image': ''},
    'Fox': {'name': 'Fox', 'image': ''},
    'Pikachu': {'name': 'Pikachu', 'image': ''},
    'Luigi': {'name': 'Luigi', 'image': ''},
    'Ness': {'name': 'Ness', 'image': ''},
    'Captain Falcon': {'name': 'Captain Falcon', 'image': ''},
    'Jigglypuff': {'name': 'Jigglypuff', 'image': ''},
    'Peach': {'name': 'Peach', 'image': ''},
    'Daisy': {'name': 'Daisy', 'image': ''},
    'Bowser': {'name': 'Bowser', 'image': ''},
    'Ice Climbers': {'name': 'Ice Climbers', 'image': ''},
    'Sheik': {'name': 'Sheik', 'image': ''},
    'Zelda': {'name': 'Zelda', 'image': ''},
    'Dr. Mario': {'name': 'Dr. Mario', 'image': ''},
    'Pichu': {'name': 'Pichu', 'image': ''},
    'Falco': {'name': 'Falco', 'image': ''},
    'Marth': {'name': 'Marth', 'image': ''},
    'Lucina': {'name': 'Lucina', 'image': ''},
    'Young Link': {'name': 'Young Link', 'image': ''},
    'Ganondorf': {'name': 'Ganondorf', 'image': ''},
    'Mewtwo': {'name': 'Mewtwo', 'image': ''},
    'Roy': {'name': 'Roy', 'image': ''},
    'Chrom': {'name': 'Chrom', 'image': ''},
    'Mr. Game & Watch': {'name': 'Mr. Game & Watch', 'image': ''},
    'Meta Knight': {'name': 'Meta Knight', 'image': ''},
    'Pit': {'name': 'Pit', 'image': ''},
    'Dark Pit': {'name': 'Dark Pit', 'image': ''},
    'Zero Suit Samus': {'name': 'Zero Suit Samus', 'image': ''},
    'Wario': {'name': 'Wario', 'image': ''},
    'Snake': {'name': 'Snake', 'image': ''},
    'Ike': {'name': 'Ike', 'image': ''},
    'Pokemon Trainer': {'name': 'Pokemon Trainer', 'image': ''},
    'Diddy Kong': {'name': 'Diddy Kong', 'image': ''},
    'Lucas': {'name': 'Lucas', 'image': ''},
    'Sonic': {'name': 'Sonic', 'image': ''},
    'King Dedede': {'name': 'King Dedede', 'image': ''},
    'Olimar': {'name': 'Olimar', 'image': ''},
    'Lucario': {'name': 'Lucario', 'image': ''},
    'R.O.B.': {'name': 'R.O.B.', 'image': ''},
    'Toon Link': {'name': 'Toon Link', 'image': ''},
    'Wolf': {'name': 'Wolf', 'image': ''},
    'Villager': {'name': 'Villager', 'image': ''},
    'Mega Man': {'name': 'Mega Man', 'image': ''},
    'Wii Fit Trainer': {'name': 'Wii Fit Trainer', 'image': ''},
    'Rosalina & Luma': {'name': 'Rosalina & Luma', 'image': ''},
    'Little Mac': {'name': 'Little Mac', 'image': ''},
    'Greninja': {'name': 'Greninja', 'image': ''},
    'Mii Brawler': {'name': 'Mii Brawler', 'image': ''},
    'Mii Swordfighter': {'name': 'Mii Swordfighter', 'image': ''},
    'Mii Gunner': {'name': 'Mii Gunner', 'image': ''},
    'Palutena': {'name': 'Palutena', 'image': ''},
    'Pac-Man': {'name': 'Pac-Man', 'image': ''},
    'Robin': {'name': 'Robin', 'image': ''},
    'Shulk': {'name': 'Shulk', 'image': ''},
    'Bowser Jr.': {'name': 'Bowser Jr.', 'image': ''},
    'Duck Hunt': {'name': 'Duck Hunt', 'image': ''},
    'Ryu': {'name': 'Ryu', 'image': ''},
    'Ken': {'name': 'Ken', 'image': ''},
    'Cloud': {'name': 'Cloud', 'image': ''},
    'Corrin': {'name': 'Corrin', 'image': ''},
    'Bayonetta': {'name': 'Bayonetta', 'image': ''},
    'Inkling': {'name': 'Inkling', 'image': ''},
    'Ridley': {'name': 'Ridley', 'image': ''},
    'Simon': {'name': 'Simon', 'image': ''},
    'Richter': {'name': 'Richter', 'image': ''},
    'King K. Rool': {'name': 'King K. Rool', 'image': ''},
    'Isabelle': {'name': 'Isabelle', 'image': ''},
    'Incineroar': {'name': 'Incineroar', 'image': ''},
    'Piranha Plant': {'name': 'Piranha Plant', 'image': ''},
    'Joker': {'name': 'Joker', 'image': ''},
    'Hero': {'name': 'Hero', 'image': ''},
    'Banjo & Kazooie': {'name': 'Banjo & Kazooie', 'image': ''},
    'Terry': {'name': 'Terry', 'image': ''},
    'Byleth': {'name': 'Byleth', 'image': ''},
    'Min Min': {'name': 'Min Min', 'image': ''},
    'Steve': {'name': 'Steve', 'image': ''},
    'Sephiroth': {'name': 'Sephiroth', 'image': ''},
    'Pyra/Mythra': {'name': 'Pyra/Mythra', 'image': ''},
    'Kazuya': {'name': 'Kazuya', 'image': ''},
    'Sora': {'name': 'Sora', 'image': ''}
}]
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
    global character_list
    dico_cookies = request.COOKIES
    dico_context = {'character_list':character_list}
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
            print("characters", form.cleaned_data['Characters'])
            print("year", form.cleaned_data['year'])
            response.set_cookie(key="character_data", value=json.dumps(
            {'character_name': request.POST['Characters'],
            'character_year': request.POST['year']}))


        return response
    else:
        form = CharacterForm()
    return render(request, "Characters/nondjangoforms.html", {'character_form': form})


