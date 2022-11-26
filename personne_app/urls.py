from django.urls import path
from personne_app.views import PersonneFormView, PersonneListView

urlpatterns = [
    path('personne/add/', PersonneFormView.as_view(), name='personne_add'),
    path('personne/list/', PersonneListView.as_view(), name='personne_list'),
]
