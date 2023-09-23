from django.shortcuts import render, get_object_or_404
from .models import NippoModel
from .forms import  NippoFormClass
from django.shortcuts import redirect

    

def ListView(request):
    template_name = "pro/list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)


def DetailView(request, pk):
     template_name = "pro/detail.html"
     ctx = {}
     #q = NippoModel.objects.get(pk=pk)
     q = get_object_or_404(NippoModel, pk=pk)
     ctx["object"] = q
     return render(request, template_name, ctx)

def CreateView(request):
    template_name="pro/form.html"
    form = NippoFormClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        company = form.cleaned_data["company"]
        company_id = form.cleaned_data["company_id"]
        company_password = form.cleaned_data["company_password"]
        obj = NippoModel(company=company, company_id=company_id, company_password=company_password)
        obj.save()
        return redirect("list")
    return render(request, template_name, ctx)

def UpdateFormView(request, pk):
    template_name = "pro/form.html"
    #obj = NippoModel.objects.get(pk=pk)
    obj = get_object_or_404(NippoModel, pk=pk)
    initial_values = {"company": obj.company, "company_id":obj.company_id, "company_password":obj.company_password}
    form = NippoFormClass(request.POST or initial_values)
    ctx = {"form": form}
    ctx["object"] = obj
    if form.is_valid():
        company = form.cleaned_data["company"]
        company_id = form.cleaned_data["company_id"]
        company_password = form.cleaned_data["company_password"]
        obj.company = company
        obj.company_id = company_id
        obj.company_password = company_password
        obj.save()
        if request.POST:
            return redirect("list")
    return render(request, template_name, ctx)

def DeleteView(request, pk):
    template_name = "pro/delete.html"
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("list")
    return render(request, template_name, ctx)





