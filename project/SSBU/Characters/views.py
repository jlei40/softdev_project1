from django.shortcuts import render
from .Character_forms import CharacterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse


import datetime
import json
character_list = [
    {
        'Mario': {
            'name': 'Mario',
            'height': "5'1\" (155 cm)",
            'weight': 'Plumber-weight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Donkey Kong': {
            'name': 'Donkey Kong',
            'height': "7'0\" (213 cm)",
            'weight': 'Heavyweight',
            'series': 'Donkey Kong',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Link': {
            'name': 'Link',
            'height': "5'7\" (170 cm)",
            'weight': 'Heroic weight',
            'series': 'The Legend of Zelda',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Samus': {
            'name': 'Samus Aran',
            'height': "6'3\" (190 cm)",
            'weight': 'Power Suit weight',
            'series': 'Metroid',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Dark Samus': {
            'name': 'Dark Samus',
            'height': "6'4\" (193 cm)",
            'weight': 'Phazon weight',
            'series': 'Metroid',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Yoshi': {
            'name': 'Yoshi',
            'height': "3'7\" (109 cm)",
            'weight': 'Lightweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Kirby': {
            'name': 'Kirby',
            'height': "8\" (20 cm)",
            'weight': 'Lightweight',
            'series': 'Kirby',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Fox': {
            'name': 'Fox McCloud',
            'height': "5'8\" (173 cm)",
            'weight': 'Middleweight',
            'series': 'Star Fox',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Pikachu': {
            'name': 'Pikachu',
            'height': "1'4\" (40 cm)",
            'weight': 'Featherweight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Luigi': {
            'name': 'Luigi',
            'height': "5'9\" (175 cm)",
            'weight': 'Plumber-weight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ness': {
            'name': 'Ness',
            'height': "4'11\" (150 cm)",
            'weight': 'Kid-weight',
            'series': 'EarthBound',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Captain Falcon': {
            'name': 'Captain Falcon',
            'height': "6'2\" (188 cm)",
            'weight': 'Middleweight',
            'series': 'F-Zero',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Jigglypuff': {
            'name': 'Jigglypuff',
            'height': "1'8\" (51 cm)",
            'weight': 'Balloon-weight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Peach': {
            'name': 'Princess Peach',
            'height': "6'0\" (183 cm)",
            'weight': 'Lightweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Daisy': {
            'name': 'Princess Daisy',
            'height': "5'11\" (180 cm)",
            'weight': 'Lightweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Bowser': {
            'name': 'Bowser',
            'height': "8'7\" (261 cm)",
            'weight': 'Super Heavyweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ice Climbers': {
            'name': 'Ice Climbers',
            'height': "3'5\" (104 cm)",
            'weight': 'Middleweight',
            'series': 'Ice Climber',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Sheik': {
            'name': 'Sheik',
            'height': "5'10\" (178 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Zelda': {
            'name': 'Princess Zelda',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Dr. Mario': {
            'name': 'Dr. Mario',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Pichu': {
            'name': 'Pichu',
            'height': "1'0\" (30 cm)",
            'weight': 'Lightweight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Falco': {
            'name': 'Falco Lombardi',
            'height': "6'2\" (188 cm)",
            'weight': 'Featherweight',
            'series': 'Star Fox',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Marth': {
            'name': 'Marth',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Lucina': {
            'name': 'Lucina',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Young Link': {
            'name': 'Young Link',
            'height': "5'6\" (168 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ganondorf': {
            'name': 'Ganondorf',
            'height': "7'6\" (229 cm)",
            'weight': 'Super Heavyweight',
            'series': 'The Legend of Zelda',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Mewtwo': {
            'name': 'Mewtwo',
            'height': "6'7\" (201 cm)",
            'weight': 'Middleweight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Roy': {
            'name': 'Roy',
            'height': "5'8\" (173 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Chrom': {
            'name': 'Chrom',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Mr. Game & Watch': {
            'name': 'Mr. Game & Watch',
            'height': "2D (Variable height)",
            'weight': 'Variable weight',
            'series': 'Game & Watch',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Meta Knight': {
            'name': 'Meta Knight',
            'height': "6'5\" (196 cm)",
            'weight': 'Middleweight',
            'series': 'Kirby',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Pit': {
            'name': 'Pit',
            'height': "5'2\" (157 cm)",
            'weight': 'Middleweight',
            'series': 'Kid Icarus',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Dark Pit': {
            'name': 'Dark Pit',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Kid Icarus',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Zero Suit Samus': {
            'name': 'Zero Suit Samus',
            'height': "5'9\" (175 cm)",
            'weight': 'Middleweight',
            'series': 'Metroid',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Wario': {
            'name': 'Wario',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Snake': {
            'name': 'Solid Snake',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Metal Gear',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ike': {
            'name': 'Ike',
            'height': "6'4\" (193 cm)",
            'weight': 'Heavyweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Pokemon Trainer': {
            'name': 'Pokémon Trainer',
            'height': "5'3\" (160 cm) (Average of the three Pokémon)",
            'weight': 'Variable weight (Depends on the active Pokémon)',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Diddy Kong': {
            'name': 'Diddy Kong',
            'height': "3'0\" (91 cm)",
            'weight': 'Featherweight',
            'series': 'Donkey Kong',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Lucas': {
            'name': 'Lucas',
            'height': "4'3\" (130 cm)",
            'weight': 'Kid-weight',
            'series': 'EarthBound',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Sonic': {
            'name': 'Sonic the Hedgehog',
            'height': "3'3\" (100 cm)",
            'weight': 'Middleweight',
            'series': 'Sonic the Hedgehog',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'King Dedede': {
            'name': 'King Dedede',
            'height': "7'3\" (221 cm)",
            'weight': 'Super Heavyweight',
            'series': 'Kirby',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Olimar': {
            'name': 'Olimar',
            'height': "1'1\" (33 cm)",
            'weight': 'Featherweight',
            'series': 'Pikmin',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Lucario': {
            'name': 'Lucario',
            'height': "3'11\" (119 cm)",
            'weight': 'Middleweight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'R.O.B.': {
            'name': 'R.O.B.',
            'height': "2'11\" (89 cm)",
            'weight': 'Heavyweight',
            'series': 'R.O.B.',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Toon Link': {
            'name': 'Toon Link',
            'height': "3'5\" (104 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Wolf': {
            'name': 'Wolf O\'Donnell',
            'height': "6'4\" (193 cm)",
            'weight': 'Middleweight',
            'series': 'Star Fox',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Villager': {
            'name': 'Villager',
            'height': "3'3\" (100 cm)",
            'weight': 'Featherweight',
            'series': 'Animal Crossing',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Mega Man': {
            'name': 'Mega Man',
            'height': "4'11\" (150 cm)",
            'weight': 'Middleweight',
            'series': 'Mega Man',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Wii Fit Trainer': {
            'name': 'Wii Fit Trainer',
            'height': "5'6\" (168 cm)",
            'weight': 'Middleweight',
            'series': 'Wii Fit',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Rosalina & Luma': {
            'name': 'Rosalina & Luma',
            'height': "7'3\" (221 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Little Mac': {
            'name': 'Little Mac',
            'height': "4'8\" (142 cm)",
            'weight': 'Featherweight',
            'series': 'Punch-Out!!',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Greninja': {
            'name': 'Greninja',
            'height': "4'11\" (150 cm)",
            'weight': 'Middleweight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Palutena': {
            'name': 'Palutena',
            'height': "6'7\" (201 cm)",
            'weight': 'Middleweight',
            'series': 'Kid Icarus',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Pac-Man': {
            'name': 'Pac-Man',
            'height': "4'0\" (122 cm)",
            'weight': 'Middleweight',
            'series': 'Pac-Man',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Robin': {
            'name': 'Robin',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Shulk': {
            'name': 'Shulk',
            'height': "5'11\" (180 cm)",
            'weight': 'Middleweight',
            'series': 'Xenoblade Chronicles',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Bowser Jr.': {
            'name': 'Bowser Jr.',
            'height': "4'0\" (122 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Duck Hunt': {
            'name': 'Duck Hunt',
            'height': "1'2\" (36 cm)",
            'weight': 'Featherweight',
            'series': 'Duck Hunt',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ryu': {
            'name': 'Ryu',
            'height': "5'9\" (175 cm)",
            'weight': 'Middleweight',
            'series': 'Street Fighter',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ken': {
            'name': 'Ken',
            'height': "5'9\" (175 cm)",
            'weight': 'Middleweight',
            'series': 'Street Fighter',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Cloud': {
            'name': 'Cloud Strife',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Final Fantasy',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Corrin': {
            'name': 'Corrin',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Bayonetta': {
            'name': 'Bayonetta',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Bayonetta',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Inkling': {
            'name': 'Inkling',
            'height': "3'7\" (109 cm)",
            'weight': 'Featherweight',
            'series': 'Splatoon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Ridley': {
            'name': 'Ridley',
            'height': "25'0\" (762 cm) (Approximate)",
            'weight': 'Super Heavyweight',
            'series': 'Metroid',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Simon': {
            'name': 'Simon Belmont',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Castlevania',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Richter': {
            'name': 'Richter Belmont',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Castlevania',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'King K. Rool': {
            'name': 'King K. Rool',
            'height': "21'0\" (640 cm) (Approximate)",
            'weight': 'Super Heavyweight',
            'series': 'Donkey Kong',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Isabelle': {
            'name': 'Isabelle',
            'height': "1'4\" (41 cm)",
            'weight': 'Lightweight',
            'series': 'Animal Crossing',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Incineroar': {
            'name': 'Incineroar',
            'height': "5'11\" (180 cm) (Approximate)",
            'weight': 'Heavyweight',
            'series': 'Pokémon',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Piranha Plant': {
            'name': 'Piranha Plant',
            'height': "Variable",
            'weight': 'Variable',
            'series': 'Super Mario',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Joker': {
            'name': 'Joker',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Persona',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Hero': {
            'name': 'Hero',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Dragon Quest',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Banjo & Kazooie': {
            'name': 'Banjo & Kazooie',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Banjo-Kazooie',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Terry Bogard': {
            'name': 'Terry Bogard',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Fatal Fury',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Byleth': {
            'name': 'Byleth',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Fire Emblem',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Min Min': {
            'name': 'Min Min',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'ARMS',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Steve': {
            'name': 'Steve',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Minecraft',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Sephiroth': {
            'name': 'Sephiroth',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Final Fantasy',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Pyra/Mythra': {
            'name': 'Pyra/Mythra',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Xenoblade Chronicles',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Kazuya Mishima': {
            'name': 'Kazuya Mishima',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Tekken',
            'image': 'INSERT IMAGE LINK HERE'
        }
    },
    {
        'Sora': {
            'name': 'Sora',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Kingdom Hearts',
            'image': 'INSERT IMAGE LINK HERE'
        }
    }
]



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
    return render(request, "Characters/character_info.html", {'character_list': character_list})

def djangoforms(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character_name = form.cleaned_data['name']
            selected_character = form.cleaned_data['Characters']

            # Check if 'action' exists in the form data
            action = form.cleaned_data['action']

            if action == 'edit':
                # Editing the character data
                for character in character_list:
                    if selected_character in character.keys():
                        character[selected_character]['name'] = character_name
                        character[selected_character]['height'] = form.cleaned_data['height']
                        character[selected_character]['weight'] = form.cleaned_data['weight']
                        character[selected_character]['series'] = form.cleaned_data['series']

            elif action == 'delete':
                # Deleting the character data
                for i, character in enumerate(character_list):
                    if selected_character in character.keys():
                        del character_list[i]
                        break

            # Redirect to the character_info view after successful form submission
            return redirect('Characters:character_info')

    else:
        form = CharacterForm()

    return render(request, "Characters/djangoforms.html", {'character_form': form})

def nondjangoforms(request):
    if request.method == "POST":
        character_name = request.POST.get('name')
        selected_character = request.POST.get('Characters')
        action = request.POST.get('action')

        if action == 'edit':
            # Editing the character data
            for character in character_list:
                if selected_character in character.keys():
                    character[selected_character]['name'] = character_name
                    character[selected_character]['height'] = request.POST.get('height')
                    character[selected_character]['weight'] = request.POST.get('weight')
                    character[selected_character]['series'] = request.POST.get('series')
        elif action == 'delete':
            # Deleting the character data
            for i, character in enumerate(character_list):
                if selected_character in character.keys():
                    del character_list[i]
                    break

        # Redirect to the character_info view after successful form submission
        return redirect('Characters:character_info')

    # Render the form template for GET requests
    return render(request, "Characters/nondjangoforms.html", {'character_list': character_list})

