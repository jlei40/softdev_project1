from django import forms

# When we will have a database, instead of having ("Keanu Reeves", "Keanu Reeves"),
# we will have (1, "Keanu Reeves") for example with 1 the id of "Keanu Reeves" in the database

class CharacterForm(forms.Form):
    ACTION_CHOICES = [('edit', 'Edit'), ('create', 'Create')]

    action = forms.ChoiceField(choices=ACTION_CHOICES, required=True)
    name = forms.CharField(max_length=100, required=True)
    Characters = forms.ChoiceField(choices=[], required=False)
    height = forms.CharField(max_length=100, required=True)
    weight = forms.CharField(max_length=100, required=True)
    series = forms.CharField(max_length=100, required=True)