from django.shortcuts import render
from . import engine, forms

# Create your views here.
def inputpage(request):
    inputform=forms.InputForm() #request.POST
    return render(request, "primes_1.html", {"formhere":inputform})

def resultspage(request):#need ato avoid to be rendered with GET
    #if request.method == 'POST':
            # create a form instance and populate it with data from the request:
    myform = forms.InputForm(request.POST)
    if myform.is_valid():
        Primelimit=myform.cleaned_data['Primelimit']
        primeslist=engine.PrimesLessThan(Primelimit)
        context={
            "primelimit":Primelimit,
            "primeslist":primeslist
        }
        return render(request, "primes_2.html",context)
    else:
        return
