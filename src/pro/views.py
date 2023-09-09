from django.shortcuts import render
from random import randint

def ListView(request):
	return render(request, "pro/list.html")



def DetailView(request):
    template_name="pro/detail.html"
    random_int = randint(1,10)
    ctx = {
        "random_number": random_int,
    }
    return render(request, template_name, ctx)

def CreateView(request):
    template_name="pro/form.html"

    if request.POST:
        company = request.POST["company"]
        company_id = request.POST["company_id"]
        company_password = request.POST["company_password"]

    #受け取った値で必要な処理を行います
        
    return render(request, template_name)