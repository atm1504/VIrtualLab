from django import forms

# Form to take input about the pendulum from the user


class DoublePendulumForm(forms.Form):
    mass_of_first_bob_in_kg = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "mass_of_first_bob", "placeholder": "1"}))
    mass_of_second_bob_in_kg = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "mass_of_second_bob", "placeholder": "1"}))
    length_of_first_string_in_m = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "length_of_first_string", "placeholder": "1"}))
    length_of_second_string_in_m = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "length_of_second_string", "placeholder": "1"}))
