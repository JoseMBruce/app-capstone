from django import forms

class BusquedaPatente(forms.Form):
    patente = forms.CharField(label = "Patente", required = True)