from django import forms

# When we will have a database, instead of having ("Keanu Reeves", "Keanu Reeves"),
# we will have (1, "Keanu Reeves") for example with 1 the id of "Keanu Reeves" in the database
Characters = [
 
]

class CharacterForm(forms.Form):
   name = forms.CharField(max_length=100, required=True)
   actors = forms.MultipleChoiceField(
       required=True,
       widget=forms.SelectMultiple,
       choices=Characters,
   )
   year = forms.IntegerField(required=True)
