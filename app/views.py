from django.shortcuts import render, get_object_or_404
from .models import Customer, Contractor


def index(request):
    return render(request, 'app/menu.html')


def contractor_cabinet(request):
    customers = Customer.objects.all()
    return render(request, 'app/customers.html', {'customers': customers})


def customer_cabinet(request):
    contractors = Contractor.objects.all()
    return render(request, 'app/contractors.html', {'contractors': contractors})


def single_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'app/single_customer.html', {'customer': customer})


def single_contractor(request, contractor_id):
    contractor = get_object_or_404(Contractor, pk=contractor_id)
    return render(request, 'app/contractor.html', {'contractor': contractor})
