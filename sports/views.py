from django.shortcuts import render, redirect, get_object_or_404
from sports.models import Sport


def home(request):
    return render(request, 'index.html')

def sport_list(request):
    sports = Sport.objects.all()
    ctx = {'sports': sports}
    return render(request, 'sports/sport_list.html', ctx)


def sport_create(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        if event_name and location and date and sport_type:
            Sport.objects.create(
                event_name=event_name,
                location=location,
                date=date,
                sport_type=sport_type
            )
            return redirect('sports:sport_list')
    return render(request, 'sports/sport_form.html')


def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    ctx = {'sport': sport}
    return render(request, 'sports/sport_detail.html', ctx)

def sport_delete(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    sport.delete()
    return redirect('sports:sport_list')

def sport_update(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        print(location, event_name, date, sport_type)
        if event_name and location and date and sport_type:
            sport.event_name = event_name
            sport.location = location
            sport.date = date
            sport.sport_type = sport_type
            sport.save()
            return redirect(sport.get_detail_url())
    ctx = {'sport': sport}
    return render(request, 'sports/sport_form.html', ctx)
