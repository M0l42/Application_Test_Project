from django.forms import ModelForm
from personne_app.models import Personne


class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['first_name', 'last_name', 'birthday']
