from django.shortcuts import render,get_object_or_404,redirect
from .models import Customer
from orders.models import OrderItem

# Create your views here.
# Features:
# - Display all customers.
# - View customer details and their orders.
# - Add, edit, delete customer.

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})
def customer_detail(request, customer_id):
    customer_info = Customer.objects.get(id=customer_id)
    orders = OrderItem.objects.all()
    return render(request, 'customers/customer_detail.html', {'customer': customer_info, 'orders': orders})
def customer_add(request):
    if request.method == "POST":
        cust_name = request.POST.get('name')
        cust_email = request.POST.get('email')
        cust_phone = request.POST.get('phone')

        Customer.objects.create(name=cust_name, email=cust_email, phone=cust_phone)
        return redirect('customer_list')

    return render(request, 'customers/customer_add.html')
def customer_edit(request, customer_id):
    customer_data = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        customer_data.name= request.POST.get('name'),
        customer_data.email = request.POST.get('email')
        customer_data.phone = request.POST.get('phone')
        customer_data.save()
        return redirect('customer_list')
    return render(request, 'customers/customer_edit.html', {'customer_data': customer_data})
def customer_delete(request, customer_id):
    customer_data = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        customer_data.delete()
        return render(request, 'customers/customer_list.html', {'customer_data': customer_data})
    return render(request, 'customers/customer_delete.html', {'customer_data': customer_data})
