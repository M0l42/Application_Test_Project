from django.shortcuts import render
from django.views.generic.edit import FormView
from personne_app.forms import PersonneForm
from personne_app.models import Personne


class PersonneFormView(FormView):
    template_name = 'personne_form.html'
    form_class = PersonneForm

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birthday = form.cleaned_data['birthday']

        personne = Personne.objects.create(first_name=first_name, last_name=last_name, birthday=birthday)
        personne.save()

        return super().form_valid(form)

