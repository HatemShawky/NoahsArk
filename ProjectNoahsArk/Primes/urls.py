from django.urls import path

from . import views

urlpatterns = [
    path('primes/results/',views.resultspage, name="primes_results_page"),
    path('primes/', views.inputpage, name='primes_input_page'),
]