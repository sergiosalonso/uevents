
from django.urls import path
from . import views
app_name='events'

urlpatterns = [
    path('event/<slug:slug>/', views.EventDetailView.as_view(), name='event'),
    path('', views.EventListView.as_view(), name='list'),

    path('create/', views.CreateEventView.as_view(), name='create'),
    path('update/<slug:slug>/', views.UpdateEventView.as_view(), name='update'),
    path('delete/<slug:slug>/', views.DeleteEventView.as_view(), name='delete'),

    path('join/<slug:slug>/', views.JoinEventView.as_view(), name='join'),
    path('leave/<slug:slug>/', views.LeaveEventView.as_view(), name='leave'),
    path('myevents/<slug:slug>/', views.MyEventsListView.as_view(), name='my-events'),
    path('created-events/<slug:slug>/', views.CreatedEventsListView.as_view(), name='created-events'),
]
