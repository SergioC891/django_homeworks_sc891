from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones_objects = Phone.objects.all().order_by('-price')
    else:
        phones_objects = Phone.objects.all()

    phones = []
    for phone in phones_objects:
        phone_item = {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'slug': phone.slug,
        }
        phones.append(phone_item)

    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):

    phone_item = {}
    if slug:
        phone = Phone.objects.get(slug=slug)
        if phone:
            phone_item = {
                'name': phone.name,
                'price': phone.price,
                'image': phone.image,
                'release_date': phone.release_date,
                'lte_exists': phone.lte_exists,
            }

    template = 'product.html'
    context = {
        'phone': phone_item
    }
    return render(request, template, context)
