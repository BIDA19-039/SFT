from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm


def homepage(request):
    projects=Customer.objects.all()
    context={'projects':projects}
    return render(request, 'projects/homepage.html', context)

def dataprocessing(request, pk):
    projectObj=Customer.objects.get(customer_id=pk)
    return render(request, 'projects/dataprocessing.html', {'dataprocessing':projectObj})

def datasummary(request):
    return render(request, 'projects/datasummary.html')

@login_required(login_url="login")
def createCustomer(request):
    form=CustomerForm()

    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context={'form':form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateCustomer(request, pk):
    project=Customer.objects.get(customer_id=pk)
    form=CustomerForm(instance=project)

    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context={'form':form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteCustomer(request, pk):
    project=Customer.objects.get(customer_id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect ('homepage')
    context={'object':project}
    return render(request, 'projects/delete_template.html', context)
