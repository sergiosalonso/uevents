from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils.text import slugify
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('s', 'Student'),
        ('t', 'Teacher' ),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    type_user = models.CharField(max_length=20, default='s',choices=USER_TYPE_CHOICES)
    profile_image= models.ImageField(upload_to='profile_image/', blank=True, null=True) #aniadir el <form method="post" enctype="multipart/form-data"> en el html
    bio = models.TextField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'slug':self.slug})

    def __str__(self):
        return self.user.username
