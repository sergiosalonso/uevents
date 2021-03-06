# Generated by Django 2.1 on 2018-09-08 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('location', models.CharField(max_length=250, verbose_name='Lugar')),
                ('description', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('hour', models.TimeField(verbose_name='Hora')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('assistants', models.ManyToManyField(through='events.Assistant', to=settings.AUTH_USER_MODEL, verbose_name='asistentes')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
            options={
                'ordering': ['created', 'updated'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='assistant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='assistant',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joinning', to=settings.AUTH_USER_MODEL),
        ),
    ]
