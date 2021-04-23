from django import forms

# Form to take input about the pendulum from the user


class SimplePendulumForm(forms.Form):
    mass_of_bob_in_kg = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "mass_of_bob_in_kg", "placeholder": "1", "value": "0.10"}))

    length_of_string_in_m = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "length_of_string_in_m", "placeholder": "1", "value": "1.00"}))

    damping_factor = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "damping_factor", "placeholder": "1", "value": "0.05"}))

    theta0_left_value = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "theta0_left_value", "placeholder": "1", "value": "0"}))

    theta0_right_value = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "theta0_right_value", "placeholder": "1", "value": "5"}))
