from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop
# Create your views here.

def Productview(request):
    pform=LaptopForm()
    if request.method == 'POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='app1/pform.html'
    context={'form':pform}
    return render(request,template_name,context)

def show(request):
    pdata=Laptop.objects.all()
    context={'pdata':pdata}
    template_name = 'app1/show.html'
    return render(request, template_name, context)


def updateview(request,id):
    person=Laptop.objects.get(id=id)
    form=LaptopForm(instance=person)
    if request.method == 'POST':
        form=LaptopForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='app1/pform.html'
    context={'form':form}
    return render(request,template_name,context)


def deleteview(request,id):
    person=Laptop.objects.get(id=id)
    person.delete()
    return redirect('show')