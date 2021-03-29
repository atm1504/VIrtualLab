from django import forms

# Form to take input about the pendulum from the user


class DoublePendulumForm(forms.Form):
    mass_of_first_bob_in_kg = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "mass_of_first_bob", "placeholder": "1", "value": "1.00"}))

    mass_of_second_bob_in_kg = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "mass_of_second_bob", "placeholder": "1", "value": "1.00"}))

    length_of_first_string_in_m = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "length_of_first_string", "placeholder": "1", "value": "1.00"}))

    length_of_second_string_in_m = forms.FloatField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "length_of_second_string", "placeholder": "1", "value": "1.00"}))

    x_axis_negative_length = forms.DecimalField(decimal_places=2, max_digits=12, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "x_axis_negative_length", "placeholder": "-2", "value": "-2.00"}))

    x_axis_positive_length = forms.DecimalField(decimal_places=2, max_digits=12, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "x_axis_positive_length", "placeholder": "2", "value": "2.00"}))

    y_axis_negative_length = forms.DecimalField(decimal_places=2, max_digits=12, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "y_axis_negative_length", "placeholder": "-2", "value": "-2.00"}))

    y_axis_positive_length = forms.DecimalField(decimal_places=2, max_digits=12, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "y_axis_positive_length", "placeholder": "2", "value": "2.00"}))
