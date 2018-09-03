from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import User, Profile
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name='Nombre')
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    location = models.CharField(max_length=250, blank=False, verbose_name='Lugar')
    description= models.TextField(max_length=500, blank=False,verbose_name='Descripcion')
    date = models.DateField(auto_now=False,auto_now_add=False, verbose_name='Fecha')
    hour = models.TimeField(auto_now=False,auto_now_add=False, verbose_name='Hora')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Creador', related_name='created_by')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    assistants = models.ManyToManyField(User, through='Assistant', verbose_name='asistentes')


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('events:event', kwargs={'slug':self.slug})

    class Meta:
        ordering=['created','updated']


class Assistant(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='joinning')
    event= models.ForeignKey(Event, on_delete=models.CASCADE)
    joined=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('events:my-events', kwargs={'user':self.pk})

class Image(models.Model):
    event = models.ForeignKey(Event,  on_delete=models.CASCADE, null= True)
    image = models.ImageField(upload_to='event_images', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)


class Tag(models.Model):
    event= models.ForeignKey(Event, on_delete=models.CASCADE, null= True)
    tag= models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.tag
