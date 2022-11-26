from django.urls import path
from personne_app.views import PersonneFormView, PersonneListView

urlpatterns = [
    path('add/', PersonneFormView.as_view(), name='personne_add'),
    path('', PersonneListView.as_view(), name='personne_list'),
]
