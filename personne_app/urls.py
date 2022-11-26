from django.urls import path
from personne_app.views import PersonneFormView

urlpatterns = [
    path('personne/add/', PersonneFormView.as_view(), name='personne_add'),
]
