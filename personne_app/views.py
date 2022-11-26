from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from personne_app.forms import PersonneForm
from personne_app.models import Personne


class PersonneFormView(FormView):
    template_name = 'personne_app/personne_form.html'
    form_class = PersonneForm

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birthday = form.cleaned_data['birthday']

        personne = Personne.objects.create(first_name=first_name, last_name=last_name, birthday=birthday)
        personne.save()

        return super().form_valid(form)


class PersonneListView(ListView):
    model = Personne
    paginate_by = 20
    ordering = ['-birthday']
    template_name = 'personne_app/personne_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Personne List'
        return context
