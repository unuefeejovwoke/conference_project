from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference

#create views here

def conference_list(request):
    conferences = [
        {'name': 'Conference 1', 'dates': 'June 1-3, 2023', 'location': 'City A'},
        {'name': 'Conference 2', 'dates': 'July 10-12, 2023', 'location': 'City B'},
        {'name': 'Conference 3', 'dates': 'July 10-12, 2023', 'location': 'City C'},
        {'name': 'Conference 4', 'dates': 'July 10-12, 2023', 'location': 'City D'},
        {'name': 'Conference 5', 'dates': 'July 10-12, 2023', 'location': 'City E'},
        # Add more dummy conference information
    ]
    return render(request, 'conference/conference_list.html', {'conferences': conferences})