from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Conference

#create views here

def conference_list(request):
    conferences = [
        {'id': 1, 'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {'id': 2, 'name': 'Conference 2', 'dates': 'July 10-12, 2023', 'location': 'City B'},
        {'id': 3, 'name': 'Conference 3', 'dates': 'July 10-12, 2023', 'location': 'City C'},
        {'id': 4, 'name': 'Conference 4', 'dates': 'July 10-12, 2023', 'location': 'City D'},
        {'id': 5, 'name': 'Conference 5', 'dates': 'July 10-12, 2023', 'location': 'City E'},
        # Add more dummy conference information
    ]
    return render(request, 'conference/conference_list.html', {'conferences': conferences})

def conference_create(request):
    return render(request, 'conference/conference_create.html')

def conference_detail(request, conference_id):
    conferences = [
        {'id': 1, 'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A', 'topics': 'Topic A, Topic B'},
        {'id': 2, 'name': 'Conference 2', 'dates': 'July 10-12, 2023', 'location': 'City B', 'topics': 'Topic C, Topic D'},
        {'id': 3, 'name': 'Conference 3', 'dates': 'July 10-12, 2023', 'location': 'City C', 'topics': 'Topic E, Topic F'},
        {'id': 4, 'name': 'Conference 4', 'dates': 'July 10-12, 2023', 'location': 'City D', 'topics': 'Topic G, Topic H'},
        {'id': 5, 'name': 'Conference 5', 'dates': 'July 10-12, 2023', 'location': 'City E', 'topics': 'Topic I, Topic J'},
    ]

    conference = None
    for conf in conferences:
        if conf['id'] == conference_id:
            conference = conf
            break

    if conference is None:
        raise Http404("Conference does not exist.")

    return render(request, 'conference/conference_detail.html', {'conference': conference})


def conference_update(request, conference_id):
    conference = {'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A', 'topics': 'Topic A, Topic B'}
    return render(request, 'conference/conference_update.html', {'conference': conference})