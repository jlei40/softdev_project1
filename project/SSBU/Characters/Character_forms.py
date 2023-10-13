from django import forms

# When we will have a database, instead of having ("Keanu Reeves", "Keanu Reeves"),
# we will have (1, "Keanu Reeves") for example with 1 the id of "Keanu Reeves" in the database
Characters = [
    ("Mario", "Mario"),
    ("Donkey Kong", "Donkey Kong"),
    ("Link", "Link"),
    ("Samus", "Samus"),
    ("Dark Samus", "Dark Samus"),
    ("Yoshi", "Yoshi"),
    ("Kirby", "Kirby"),
    ("Fox", "Fox"),
    ("Pikachu", "Pikachu"),
    ("Luigi", "Luigi"),
    ("Ness", "Ness"),
    ("Captain Falcon", "Captain Falcon"),
    ("Jigglypuff", "Jigglypuff"),
    ("Peach", "Peach"),
    ("Daisy", "Daisy"),
    ("Bowser", "Bowser"),
    ("Ice Climbers", "Ice Climbers"),
    ("Sheik", "Sheik"),
    ("Zelda", "Zelda"),
    ("Dr. Mario", "Dr. Mario"),
    ("Pichu", "Pichu"),
    ("Falco", "Falco"),
    ("Marth", "Marth"),
    ("Lucina", "Lucina"),
    ("Young Link", "Young Link"),
    ("Ganondorf", "Ganondorf"),
    ("Mewtwo", "Mewtwo"),
    ("Roy", "Roy"),
    ("Chrom", "Chrom"),
    ("Mr. Game & Watch", "Mr. Game & Watch"),
    ("Meta Knight", "Meta Knight"),
    ("Pit", "Pit"),
    ("Dark Pit", "Dark Pit"),
    ("Zero Suit Samus", "Zero Suit Samus"),
    ("Wario", "Wario"),
    ("Snake", "Snake"),
    ("Ike", "Ike"),
    ("Pokemon Trainer", "Pokemon Trainer"),
    ("Diddy Kong", "Diddy Kong"),
    ("Lucas", "Lucas"),
    ("Sonic", "Sonic"),
    ("King Dedede", "King Dedede"),
    ("Olimar", "Olimar"),
    ("Lucario", "Lucario"),
    ("R.O.B.", "R.O.B."),
    ("Toon Link", "Toon Link"),
    ("Wolf", "Wolf"),
    ("Villager", "Villager"),
    ("Mega Man", "Mega Man"),
    ("Wii Fit Trainer", "Wii Fit Trainer"),
    ("Rosalina & Luma", "Rosalina & Luma"),
    ("Little Mac", "Little Mac"),
    ("Greninja", "Greninja"),
    ("Palutena", "Palutena"),
    ("Pac-Man", "Pac-Man"),
    ("Robin", "Robin"),
    ("Shulk", "Shulk"),
    ("Bowser Jr.", "Bowser Jr."),
    ("Duck Hunt", "Duck Hunt"),
    ("Ryu", "Ryu"),
    ("Ken", "Ken"),
    ("Cloud", "Cloud"),
    ("Corrin", "Corrin"),
    ("Bayonetta", "Bayonetta"),
    ("Inkling", "Inkling"),
    ("Ridley", "Ridley"),
    ("Simon", "Simon"),
    ("Richter", "Richter"),
    ("King K. Rool", "King K. Rool"),
    ("Isabelle", "Isabelle"),
    ("Incineroar", "Incineroar"),
    ("Piranha Plant", "Piranha Plant"),
    ("Joker", "Joker"),
    ("Hero", "Hero"),
    ("Banjo & Kazooie", "Banjo & Kazooie"),
    ("Terry Bogard", "Terry Bogard"),
    ("Byleth", "Byleth"),
    ("Min Min", "Min Min"),
    ("Steve", "Steve"),
    ("Sephiroth", "Sephiroth"),
    ("Pyra/Mythra", "Pyra/Mythra"),
    ("Kazuya Mishima", "Kazuya Mishima")
]

class CharacterForm(forms.Form):
    ACTION_CHOICES = [('edit', 'Edit'), ('delete', 'Delete')]

    action = forms.ChoiceField(choices=ACTION_CHOICES, required=True)
    name = forms.CharField(max_length=100, required=True)
    Characters = forms.ChoiceField(choices=Characters, required=False)
    height = forms.CharField(max_length=100, required=True)
    weight = forms.CharField(max_length=100, required=True)
    series = forms.CharField(max_length=100, required=True)