from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Trip
from ..login.models import User
from .forms import TripForm



# Create your views here.
def index(request):
    print "#"*50
    print "sessionvars - user_name: {}, id: {}".format(request.session['user_name'], request.session['user_id'])
    myTrips = Trip.objects.filter(participant=request.session['user_id'])
    print "*"*50
    print "mytrips length: {}".format(len(myTrips))
    otherTrips = Trip.objects.exclude(participant=request.session['user_id'])
    context = {'otherTrips': otherTrips, 'myTrips': myTrips}
    return render(request, 'travelbuddy/index.html', context)

def new(request):
    tripForm = TripForm()
    context = {'tripForm': tripForm}

    return render(request, 'travelbuddy/new.html', context)

def create(request):
    if request.method == 'POST':
        current_user = User.objects.get(id=request.session['user_id'])
        owner = Trip(owner=current_user)
        tripForm = TripForm(request.POST, instance=owner)
        if tripForm.is_valid():
            newTrip = tripForm.save()
            newTrip.participant.add(current_user)
            print "*"*50
            print "newTrip: {}".format(newTrip)
            return redirect(reverse('travelbuddy:index'))
        else:
            print 'tripform not valid'
            context = {'tripForm': tripForm}
            return render(request, 'travelbuddy/new.html', context)
    else:
        print "*"*50
        print "trip else runs"
        tripForm = TripForm()
        context = {'tripForm': tripForm}
        return render(request, 'travelbuddy/new.html', context)

    return redirect(reverse('travelbuddy:index'))

def show(request, id):
    thisTrip = Trip.objects.get(id=id)
    # print "^"*50
    # print len(User.objects.filter(trip__id=id).exclude(trip__owner=request.session['user_id']))
    otherParticipants = User.objects.filter(participantToTrip__id=id).exclude(username=thisTrip.owner.username)
    context = {'thisTrip': thisTrip, 'otherParticipants': otherParticipants}
    return render(request, 'travelbuddy/show.html', context)

def join(request, trip_id):
    current_user = User.objects.get(id=request.session['user_id'])
    current_trip = Trip.objects.get(id=trip_id)
    current_trip.participant.add(current_user)
    return redirect(reverse('travelbuddy:index'))
