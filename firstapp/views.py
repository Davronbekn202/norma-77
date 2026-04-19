from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Product


@permission_required('firstapp.add_product', raise_exception=False)
def product_create(request):
    if not request.user.has_perm('firstapp.add_product'):
        return HttpResponse("Sizda ruxsat yo‘q")

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Product.objects.create(name=name, price=price)
        return redirect('success')

    return render(request, 'products.html')

def noproduct(request):
    return render(request,'nopermission')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    info = Product.objects.all()
    return render(request, 'success.html',{"forms":info})
