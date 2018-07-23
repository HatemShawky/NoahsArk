from django.urls import path

from . import views

urlpatterns = [
    path('pizza/results/',views.resultspage, name="pizza_results_page"),
    path('pizza/', views.inputpage, name='pizza_input_page'),
]