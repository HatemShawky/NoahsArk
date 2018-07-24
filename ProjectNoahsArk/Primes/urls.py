from django.urls import path

from . import views

urlpatterns = [
    path('results/',views.resultspage, name="primes_results_page"),
    path('input/', views.inputpage, name='primes_input_page'),
]
