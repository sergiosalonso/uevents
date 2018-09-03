from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event, Image, Tag, Assistant
from django.contrib import messages

class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ('name', 'location', 'description', 'date', 'hour')
    template_name='events/event_form.html'
    def get_success_url(self):
        return reverse('events:event', kwargs={'slug' : self.object.slug})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

class UpdateEventView(LoginRequiredMixin,UpdateView):
    model = Event
    fields = ('name', 'location', 'description', 'date', 'hour')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator_id=self.request.user.id)

class DeleteEventView(LoginRequiredMixin,DeleteView):
    model=Event
    success_url= reverse_lazy('events:list')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator_id=self.request.user.id)


class EventListView(ListView):
    model=Event

class EventDetailView(LoginRequiredMixin,DetailView):
    model=Event
    template_name='events/event_detail.html'


class JoinEventView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("events:event", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, slug=self.kwargs.get("slug"))

        try:
            Assistant.objects.create(user=self.request.user,event=event)

        except IntegrityError:
            messages.warning(self.request,("Warning, already joined to {}".format(event.name)))

        else:
            messages.success(self.request,"You are now going to {}.".format(event.name))

            return super().get(request, *args, **kwargs)


class LeaveEventView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("events:list")

    def get(self, request, *args, **kwargs):
        try:

            assistant = Assistant.objects.filter(
            user=self.request.user,
            event__slug=self.kwargs.get("slug")
            ).get()

        except Assistant.DoesNotExist:
            messages.warning(
            self.request,
            "You can't leave this event because you aren't in it."
            )
        else:
            assistant.delete()
            messages.success(
            self.request,
            "You have successfully leave this event."
            )
            return super().get(request, *args, **kwargs)
class MyEventsListView(LoginRequiredMixin, ListView):
    model=Event
    context_object_name='my_events'
    template_name='events/my_events.html'

class CreatedEventsListView(LoginRequiredMixin, ListView):
    model=Event
    context_object_name='created_events'
    template_name='events/created_events.html'
