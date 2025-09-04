from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu

def displaying(request):
    menu_items = Menu.objects.all()
    return render(request, 'menus/display.html', {"menu_items": menu_items})


def adding(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        new_item = Menu(name=name, price=price, description=description)
        new_item.save()
        return render(request, 'menus/display.html', {"menu_items": Menu.objects.all()})
    return render(request, 'menus/adding.html')


def editing(request, ids):
    item_info = get_object_or_404(Menu, id=ids)

    if request.method == "POST":
        item_info.name = request.POST.get('name')
        item_info.price = request.POST.get('price')
        item_info.description = request.POST.get('description')
        item_info.save()
        return render(request, 'menus/display.html', {"menu_items": Menu.objects.all})
    return render(request, 'menus/edit.html', {"item_info": item_info})

# Delete an item
def deleting(request, ids):
    item_info = get_object_or_404(Menu, id=ids)
    if request.method == "POST":
        item_info.delete()
        return render(request, 'menus/display.html', {"menu_items": Menu.objects.all()})
    return render(request, 'menus/delete.html', {"item_info": item_info})
