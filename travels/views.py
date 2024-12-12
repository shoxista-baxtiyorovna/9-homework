from django.shortcuts import render, redirect, get_object_or_404
from .models import Travel


def home(request):
    return render(request, 'index.html')

def travel_list(request):
    travels = Travel.objects.all()
    ctx = {'travels': travels}
    return render(request, 'travels/travel_list.html', ctx)


def travel_create(request):
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        pop_season = request.POST.get('pop_season')
        if destination_name and country and description and pop_season:
            Travel.objects.create(
                destination_name=destination_name,
                country=country,
                description=description,
                pop_season=pop_season
            )
            return redirect('travels:travel_list')
    return render(request, 'travels/travel_form.html')


def travel_detail(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)
    ctx = {'travel': travel}
    return render(request, 'travels/travel_detail.html', ctx)

def travel_delete(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)
    travel.delete()
    return redirect('travels:travel_list')

def travel_update(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        pop_season = request.POST.get('pop_season')
        if destination_name and country and description and pop_season:
            travel.destination_name = destination_name
            travel.country = country
            travel.description = description
            travel.pop_season = pop_season
            travel.save()
            return redirect(travel.get_detail_url())
    ctx = {'travel': travel}
    return render(request, 'travels/travel_form.html', ctx)

