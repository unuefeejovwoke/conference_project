from django.urls import path
from . import views

app_name = 'conference'

urlpatterns = [
    path('', views.conference_list, name='conference_list'),
    path('conferences/create/', views.conference_create, name='conference_create'),
    path('conferences/<int:conference_id>/', views.conference_detail, name='conference_detail'),
    # path('conferences/<int:conference_id>/update/', views.conference_update, name='conference_update'),
    # path('conferences/<int:conference_id>/delete/', views.conference_delete, name='conference_delete'),
]
