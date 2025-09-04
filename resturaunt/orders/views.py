from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem

# Step 1: Create a new order
def creating(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # Customer linking can be added if needed
        new_order = Order.objects.create(name=name, phone=phone)

        return redirect('addingItems', order_id=new_order.id)

    return render(request, 'orders/creating.html')


# Step 2: Add items to an existing order
def addingItems(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        item_name = request.POST.get('item_name')
        item_quantity = int(request.POST.get('item_quantity', 1))
        price = float(request.POST.get('price', 0.00))  # ensure price is included

        OrderItem.objects.create(
            order=order,
            item_name=item_name,
            item_quantity=item_quantity,
            price=price
        )

        return redirect('displaying', order_id=order.id)

    return render(request, 'orders/adding.html', {
        "order": order,
        "order_items": order.items.all()  # show items as they are added
    })


# Step 3: Display the order and its items
def displaying(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()

    return render(request, 'orders/displaying.html', {
        "order": order,
        "order_items": order_items,

    })

