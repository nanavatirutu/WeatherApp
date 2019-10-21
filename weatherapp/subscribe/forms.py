"""
Filename:forms.py
Created on: Oct 18, 2019

Details: Helps to render forms
"""
from django import forms
import pandas as pd


cities = pd.read_csv('weatherapp/static/cities_100.csv')[['0','1']]
cities = cities.values.tolist()



class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    location  = forms.ChoiceField(choices=cities)
