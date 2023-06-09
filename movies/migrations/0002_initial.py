# Generated by Django 4.2.2 on 2023-06-12 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='countries',
            field=models.ManyToManyField(to='movies.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='persons',
            field=models.ManyToManyField(to='movies.person'),
        ),
    ]
