# Generated by Django 3.2.8 on 2021-10-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
        migrations.AddField(
            model_name='review',
            name='actors',
            field=models.ManyToManyField(related_name='reviews', to='movies.Actor'),
        ),
    ]
