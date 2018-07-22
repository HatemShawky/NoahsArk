from django.urls import path

from . import views

urlpatterns = [
    path('pizza/results/',views.resultspage, name="results_page"),
    path('pizza/', views.inputpage, name='input_page'),
]