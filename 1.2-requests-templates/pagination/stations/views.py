from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader
from django.core.paginator import Paginator

stations = []
with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        station = {
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District'],
        }
        stations.append(station)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    try:
        current_page = int(request.GET.get('page', 1))
    except Exception:
        current_page = 1

    paginator = Paginator(stations, 10)
    page = paginator.get_page(current_page)

    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
