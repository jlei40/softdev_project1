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
            'image': '/images/150px-Mario_SSBU.png'
        }
    },
    {
        'Donkey Kong': {
            'name': 'Donkey Kong',
            'height': "7'0\" (213 cm)",
            'weight': 'Heavyweight',
            'series': 'Donkey Kong',
            'image': '/images/150px-Donkey_Kong_SSBU.png'
        }
    },
    {
        'Link': {
            'name': 'Link',
            'height': "5'7\" (170 cm)",
            'weight': 'Heroic weight',
            'series': 'The Legend of Zelda',
            'image': '/images/150px-Link_SSBU.png'
        }
    },
    {
        'Samus': {
            'name': 'Samus Aran',
            'height': "6'3\" (190 cm)",
            'weight': 'Power Suit weight',
            'series': 'Metroid',
            'image': '/images/150px-Samus_SSBU.png'
        }
    },
    {
        'Dark Samus': {
            'name': 'Dark Samus',
            'height': "6'4\" (193 cm)",
            'weight': 'Phazon weight',
            'series': 'Metroid',
            'image': '/images/150px-Dark_Samus_SSBU.jpeg'
        }
    },
    {
        'Yoshi': {
            'name': 'Yoshi',
            'height': "3'7\" (109 cm)",
            'weight': 'Lightweight',
            'series': 'Super Mario',
            'image': '/images/150px-Yoshi_SSBU.png'
        }
    },
    {
        'Kirby': {
            'name': 'Kirby',
            'height': "8\" (20 cm)",
            'weight': 'Lightweight',
            'series': 'Kirby',
            'image': '/images/150px-Kirby_SSBU.png'
        }
    },
    {
        'Fox': {
            'name': 'Fox McCloud',
            'height': "5'8\" (173 cm)",
            'weight': 'Middleweight',
            'series': 'Star Fox',
            'image': '/images/150px-Fox_SSBU.png'
        }
    },
    {
        'Pikachu': {
            'name': 'Pikachu',
            'height': "1'4\" (40 cm)",
            'weight': 'Featherweight',
            'series': 'Pokémon',
            'image': '/images/150px-Pikachu_SSBU.png'
        }
    },
    {
        'Luigi': {
            'name': 'Luigi',
            'height': "5'9\" (175 cm)",
            'weight': 'Plumber-weight',
            'series': 'Super Mario',
            'image': '/images/137px-Luigi_SSBU.png'
        }
    },
    {
        'Ness': {
            'name': 'Ness',
            'height': "4'11\" (150 cm)",
            'weight': 'Kid-weight',
            'series': 'EarthBound',
            'image': '/images/150px-Ness_SSBU.png'
        }
    },
    {
        'Captain Falcon': {
            'name': 'Captain Falcon',
            'height': "6'2\" (188 cm)",
            'weight': 'Middleweight',
            'series': 'F-Zero',
            'image': '/images/150px-Captain_Falcon_SSBU.png'
        }
    },
    {
        'Jigglypuff': {
            'name': 'Jigglypuff',
            'height': "1'8\" (51 cm)",
            'weight': 'Balloon-weight',
            'series': 'Pokémon',
            'image': '/images/150px-Jigglypuff_SSBU.png'
        }
    },
    {
        'Peach': {
            'name': 'Princess Peach',
            'height': "6'0\" (183 cm)",
            'weight': 'Lightweight',
            'series': 'Super Mario',
            'image': '/images/133px-Peach_SSBU.png'
        }
    },
    {
        'Daisy': {
            'name': 'Princess Daisy',
            'height': "5'11\" (180 cm)",
            'weight': 'Lightweight',
            'series': 'Super Mario',
            'image': '/images/150px-Princess_Daisy_SSBU.jpeg'
        }
    },
    {
        'Bowser': {
            'name': 'Bowser',
            'height': "8'7\" (261 cm)",
            'weight': 'Super Heavyweight',
            'series': 'Super Mario',
            'image': '/images/150px-Bowser_SSBU.png'
        }
    },
    {
        'Ice Climbers': {
            'name': 'Ice Climbers',
            'height': "3'5\" (104 cm)",
            'weight': 'Middleweight',
            'series': 'Ice Climber',
            'image': '/images/150px-Ice_Climbers_SSBU.png'
        }
    },
    {
        'Sheik': {
            'name': 'Sheik',
            'height': "5'10\" (178 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': '/images/150px-Sheik_SSBU.png'
        }
    },
    {
        'Zelda': {
            'name': 'Princess Zelda',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': '/images/150px-Zelda_SSBU.png'
        }
    },
    {
        'Dr. Mario': {
            'name': 'Dr. Mario',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': '/images/150px-Dr.png'
        }
    },
    {
        'Pichu': {
            'name': 'Pichu',
            'height': "1'0\" (30 cm)",
            'weight': 'Lightweight',
            'series': 'Pokémon',
            'image': '/images/150px-Pichu_SSBU.png'
        }
    },
    {
        'Falco': {
            'name': 'Falco Lombardi',
            'height': "6'2\" (188 cm)",
            'weight': 'Featherweight',
            'series': 'Star Fox',
            'image': '/images/150px-Falco_SSBU.png'
        }
    },
    {
        'Marth': {
            'name': 'Marth',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Marth_SSBU.png'
        }
    },
    {
        'Lucina': {
            'name': 'Lucina',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Lucina_SSBU.png'
        }
    },
    {
        'Young Link': {
            'name': 'Young Link',
            'height': "5'6\" (168 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': '/images/150px-Young_Link_SSBU.png'
        }
    },
    {
        'Ganondorf': {
            'name': 'Ganondorf',
            'height': "7'6\" (229 cm)",
            'weight': 'Super Heavyweight',
            'series': 'The Legend of Zelda',
            'image': '/images/149px-Ganondorf_SSBU.png'
        }
    },
    {
        'Mewtwo': {
            'name': 'Mewtwo',
            'height': "6'7\" (201 cm)",
            'weight': 'Middleweight',
            'series': 'Pokémon',
            'image': '/images/149px-Mewtwo_SSBU.png'
        }
    },
    {
        'Roy': {
            'name': 'Roy',
            'height': "5'8\" (173 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Roy_SSBU.png'
        }
    },
    {
        'Chrom': {
            'name': 'Chrom',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Chrom_SSBU.jpeg'
        }
    },
    {
        'Mr. Game & Watch': {
            'name': 'Mr. Game & Watch',
            'height': "2D (Variable height)",
            'weight': 'Variable weight',
            'series': 'Game & Watch',
            'image': '/images/150px-Mr.png'
        }
    },
    {
        'Meta Knight': {
            'name': 'Meta Knight',
            'height': "6'5\" (196 cm)",
            'weight': 'Middleweight',
            'series': 'Kirby',
            'image': '/images/150px-Kirby_SSBU.png'
        }
    },
    {
        'Pit': {
            'name': 'Pit',
            'height': "5'2\" (157 cm)",
            'weight': 'Middleweight',
            'series': 'Kid Icarus',
            'image': '/images/150px-Pit_SSBU.png'
        }
    },
    {
        'Dark Pit': {
            'name': 'Dark Pit',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Kid Icarus',
            'image': '/images/142px-Dark_Pit_SSBU.png'
        }
    },
    {
        'Zero Suit Samus': {
            'name': 'Zero Suit Samus',
            'height': "5'9\" (175 cm)",
            'weight': 'Middleweight',
            'series': 'Metroid',
            'image': '/images/150px-Zero_Suit_Samus_SSBU.png'
        }
    },
    {
        'Wario': {
            'name': 'Wario',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': '/images/150px-Wario_SSBU.png'
        }
    },
    {
        'Snake': {
            'name': 'Solid Snake',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Metal Gear',
            'image': 'images/123px-Snake_SSBU.png'
        }
    },
    {
        'Ike': {
            'name': 'Ike',
            'height': "6'4\" (193 cm)",
            'weight': 'Heavyweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Ike_SSBU.png'
        }
    },
    {
        'Pokemon Trainer': {
            'name': 'Pokémon Trainer',
            'height': "5'3\" (160 cm) (Average of the three Pokémon)",
            'weight': 'Variable weight (Depends on the active Pokémon)',
            'series': 'Pokémon',
            'image': '/images/150px-Charizard_SSBU.png'
        }
    },
    {
        'Diddy Kong': {
            'name': 'Diddy Kong',
            'height': "3'0\" (91 cm)",
            'weight': 'Featherweight',
            'series': 'Donkey Kong',
            'image': '/images/145px-Diddy_Kong_SSBU.png'
        }
    },
    {
        'Lucas': {
            'name': 'Lucas',
            'height': "4'3\" (130 cm)",
            'weight': 'Kid-weight',
            'series': 'EarthBound',
            'image': '/images/150px-Lucas_SSBU.png'
        }
    },
    {
        'Sonic': {
            'name': 'Sonic the Hedgehog',
            'height': "3'3\" (100 cm)",
            'weight': 'Middleweight',
            'series': 'Sonic the Hedgehog',
            'image': '/images/150px-Sonic_SSBU.png'
        }
    },
    {
        'King Dedede': {
            'name': 'King Dedede',
            'height': "7'3\" (221 cm)",
            'weight': 'Super Heavyweight',
            'series': 'Kirby',
            'image': '/images/150px-King_Dedede_SSBU.png'
        }
    },
    {
        'Olimar': {
            'name': 'Olimar',
            'height': "1'1\" (33 cm)",
            'weight': 'Featherweight',
            'series': 'Pikmin',
            'image': '/images/150px-Olimar_SSBU.png'
        }
    },
    {
        'Lucario': {
            'name': 'Lucario',
            'height': "3'11\" (119 cm)",
            'weight': 'Middleweight',
            'series': 'Pokémon',
            'image': '/images/150px-Lucario_SSBU.png'
        }
    },
    {
        'R.O.B.': {
            'name': 'R.O.B.',
            'height': "2'11\" (89 cm)",
            'weight': 'Heavyweight',
            'series': 'R.O.B.',
            'image': '/images/150px-R.png'
        }
    },
    {
        'Toon Link': {
            'name': 'Toon Link',
            'height': "3'5\" (104 cm)",
            'weight': 'Middleweight',
            'series': 'The Legend of Zelda',
            'image': '/images/142px-Toon_Link_SSBU.png'
        }
    },
    {
        'Wolf': {
            'name': 'Wolf O\'Donnell',
            'height': "6'4\" (193 cm)",
            'weight': 'Middleweight',
            'series': 'Star Fox',
            'image': '/images/150px-Wolf_SSBU.png'
        }
    },
    {
        'Villager': {
            'name': 'Villager',
            'height': "3'3\" (100 cm)",
            'weight': 'Featherweight',
            'series': 'Animal Crossing',
            'image': '/images/150px-Villager_SSBU.png'
        }
    },
    {
        'Mega Man': {
            'name': 'Mega Man',
            'height': "4'11\" (150 cm)",
            'weight': 'Middleweight',
            'series': 'Mega Man',
            'image': '/images/150px-Mega_Man_SSBU.png'
        }
    },
    {
        'Wii Fit Trainer': {
            'name': 'Wii Fit Trainer',
            'height': "5'6\" (168 cm)",
            'weight': 'Middleweight',
            'series': 'Wii Fit',
            'image': '/images/150px-Wii_Fit_Trainer_SSBU.png'
        }
    },
    {
        'Rosalina & Luma': {
            'name': 'Rosalina & Luma',
            'height': "7'3\" (221 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': '/images/150px-Rosalina_&_Luma_SSBU.png'
        }
    },
    {
        'Little Mac': {
            'name': 'Little Mac',
            'height': "4'8\" (142 cm)",
            'weight': 'Featherweight',
            'series': 'Punch-Out!!',
            'image': '/images/150px-Little_Mac_SSBU.png'
        }
    },
    {
        'Greninja': {
            'name': 'Greninja',
            'height': "4'11\" (150 cm)",
            'weight': 'Middleweight',
            'series': 'Pokémon',
            'image': '/images/150px-Greninja_SSBU.png'
        }
    },
    {
        'Palutena': {
            'name': 'Palutena',
            'height': "6'7\" (201 cm)",
            'weight': 'Middleweight',
            'series': 'Kid Icarus',
            'image': '/images/142px-Palutena_SSBU.png'
        }
    },
    {
        'Pac-Man': {
            'name': 'Pac-Man',
            'height': "4'0\" (122 cm)",
            'weight': 'Middleweight',
            'series': 'Pac-Man',
            'image': '/images/150px-Pac-Man_SSBU.png'
        }
    },
    {
        'Robin': {
            'name': 'Robin',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Robin_SSBU.png'
        }
    },
    {
        'Shulk': {
            'name': 'Shulk',
            'height': "5'11\" (180 cm)",
            'weight': 'Middleweight',
            'series': 'Xenoblade Chronicles',
            'image': '/images/150px-Shulk_SSBU.png'
        }
    },
    {
        'Bowser Jr.': {
            'name': 'Bowser Jr.',
            'height': "4'0\" (122 cm)",
            'weight': 'Middleweight',
            'series': 'Super Mario',
            'image': '/images/150px-Bowser_jr.png'
        }
    },
    {
        'Duck Hunt': {
            'name': 'Duck Hunt',
            'height': "1'2\" (36 cm)",
            'weight': 'Featherweight',
            'series': 'Duck Hunt',
            'image': '/images/150px-Duck_Hunt_SSBU.png'
        }
    },
    {
        'Ryu': {
            'name': 'Ryu',
            'height': "5'9\" (175 cm)",
            'weight': 'Middleweight',
            'series': 'Street Fighter',
            'image': '/images/150px-Ryu_SSBU.png'
        }
    },
    {
        'Ken': {
            'name': 'Ken',
            'height': "5'9\" (175 cm)",
            'weight': 'Middleweight',
            'series': 'Street Fighter',
            'image': '/images/150px-Ken_SSBU.jpeg'
        }
    },
    {
        'Cloud': {
            'name': 'Cloud Strife',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Final Fantasy',
            'image': '/images/150px-Cloud_SSBU.png'
        }
    },
    {
        'Corrin': {
            'name': 'Corrin',
            'height': "5'7\" (170 cm)",
            'weight': 'Middleweight',
            'series': 'Fire Emblem',
            'image': '/images/150px-Corrin_SSBU.png'
        }
    },
    {
        'Bayonetta': {
            'name': 'Bayonetta',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Bayonetta',
            'image': '/images/150px-Bayonetta_SSBU.png'
        }
    },
    {
        'Inkling': {
            'name': 'Inkling',
            'height': "3'7\" (109 cm)",
            'weight': 'Featherweight',
            'series': 'Splatoon',
            'image': '/images/150px-Inkling_SSBU.jpeg'
        }
    },
    {
        'Ridley': {
            'name': 'Ridley',
            'height': "25'0\" (762 cm) (Approximate)",
            'weight': 'Super Heavyweight',
            'series': 'Metroid',
            'image': '/images/150px-Ridley_SSBU.jpeg'
        }
    },
    {
        'Simon': {
            'name': 'Simon Belmont',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Castlevania',
            'image': '/images/150px-Simon_SSBU.jpeg'
        }
    },
    {
        'Richter': {
            'name': 'Richter Belmont',
            'height': "6'0\" (183 cm)",
            'weight': 'Middleweight',
            'series': 'Castlevania',
            'image': '/images/150px-Richter_SSBU.jpeg'
        }
    },
    {
        'King K. Rool': {
            'name': 'King K. Rool',
            'height': "21'0\" (640 cm) (Approximate)",
            'weight': 'Super Heavyweight',
            'series': 'Donkey Kong',
            'image': '/images/150px-King_K_Rool_SSBU.jpeg'
        }
    },
    {
        'Isabelle': {
            'name': 'Isabelle',
            'height': "1'4\" (41 cm)",
            'weight': 'Lightweight',
            'series': 'Animal Crossing',
            'image': '/images/150px-Isabelle_SSBU.jpeg'
        }
    },
    {
        'Incineroar': {
            'name': 'Incineroar',
            'height': "5'11\" (180 cm) (Approximate)",
            'weight': 'Heavyweight',
            'series': 'Pokémon',
            'image': '/images/150px-Incineroar_SSBU.jpeg'
        }
    },
    {
        'Piranha Plant': {
            'name': 'Piranha Plant',
            'height': "Variable",
            'weight': 'Variable',
            'series': 'Super Mario',
            'image': '/images/150px-Piranha_Plant_SSBU.jpeg'
        }
    },
    {
        'Joker': {
            'name': 'Joker',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Persona',
            'image': '/images/150px-Joker_SSBU.jpeg'
        }
    },
    {
        'Hero': {
            'name': 'Hero',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Dragon Quest',
            'image': '/images/150px-Hero_SSBU.jpeg'
        }
    },
    {
        'Banjo & Kazooie': {
            'name': 'Banjo & Kazooie',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Banjo-Kazooie',
            'image': '/images/150px-Banjo_&_Kazooie_SSBU.jpeg'
        }
    },
    {
        'Terry Bogard': {
            'name': 'Terry Bogard',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Fatal Fury',
            'image': '/images/150px-Terry_SSBU.jpeg'
        }
    },
    {
        'Byleth': {
            'name': 'Byleth',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Fire Emblem',
            'image': '/images/150px-Byleth_SSBU.jpeg'
        }
    },
    {
        'Min Min': {
            'name': 'Min Min',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'ARMS',
            'image': '/images/150px-Min_Min_SSBU.jpeg'
        }
    },
    {
        'Steve': {
            'name': 'Steve',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Minecraft',
            'image': '/images/150px-Steve_SSBU.jpeg'
        }
    },
    {
        'Sephiroth': {
            'name': 'Sephiroth',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Final Fantasy',
            'image': '/images/150px-Sephiroth_SSBU.jpeg'
        }
    },
    {
        'Pyra/Mythra': {
            'name': 'Pyra/Mythra',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Xenoblade Chronicles',
            'image': '/images/150px-Pyra_Mythra_SSBU.jpeg'
        }
    },
    {
        'Kazuya Mishima': {
            'name': 'Kazuya Mishima',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Tekken',
            'image': '/images/150px-Kazuya_SSBU.jpeg'
        }
    },
    {
        'Sora': {
            'name': 'Sora',
            'height': "Unknown",
            'weight': 'Unknown',
            'series': 'Kingdom Hearts',
            'image': '/images/150px-Sora_SSBU.jpeg'
        }
    }
]



# Create your views here.

def index(request):
    title_page = 'Characters Index' 
    return render(request, 'Characters/index.html',
        context = {'title_page' : title_page,
                    })
    
def searched(request):
    return render(request, 'Characters/searched.html',
    )
    
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

def search(request):
    selected_character_info = None

    if request.method == "POST":
        selected_character_name = request.POST.get('selected_character')  # Use the correct field name

        # Find the selected character's information from the character_list
        for character_dict in character_list:
            for character_name, character_info in character_dict.items():
                if character_name == selected_character_name:
                    selected_character_info = character_info
                    break

        # Render the searched.html template with the selected character's information
        return render(request, "Characters/searched.html", {
            'selected_character': selected_character_info,
        })

    # Render the search.html template for GET requests
    return render(request, "Characters/search.html", {'character_list': character_list})