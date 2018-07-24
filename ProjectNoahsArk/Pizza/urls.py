from django.urls import path

from . import views

urlpatterns = [
    path('results/',views.resultspage, name="pizza_results_page"),
    path('input/', views.inputpage, name='pizza_input_page'),
]
