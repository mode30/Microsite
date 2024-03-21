from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import  CustomerForm
from .models import Customer
# Create your views here.
def index(request):
    form=CustomerForm()
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponse('index')
        else:
            form=CustomerForm()
            
    return render(request,'signup/index.html',{
        'form':form
    })
    
def name(request):
    objects=Customer.objects.all().values_list('full_name',flat=True)
    
    names=list(objects)
    return render(request,'signup/names.html',{
        'name':names
    })