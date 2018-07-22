from django.shortcuts import render
from . import engine, forms


# Create your views here.
def inputpage(request):
    inputform=forms.InputForm() #request.POST
    return render(request, "pizza_1.html", {"formhere":inputform})

def resultspage(request):#need ato avoid to be rendered with GET
    #if request.method == 'POST':
            # create a form instance and populate it with data from the request:
    myform = forms.InputForm(request.POST)
    if myform.is_valid():
        pizza1=engine.Pizza(myform.cleaned_data['Pizza1_r'],myform.cleaned_data['Pizza1_h'],myform.cleaned_data['Pizza1_p'])
        pizza2=engine.Pizza(myform.cleaned_data['Pizza2_r'],myform.cleaned_data['Pizza2_h'],myform.cleaned_data['Pizza2_p'])
        context={
            "VPRatio1":pizza1.getratio(),
            "VPRatio2":pizza2.getratio(),
            "diff":pizza1-pizza2
        }
        return render(request, "pizza_2.html",context)
    else:
        return
    