# Generated by Django 3.2.7 on 2021-09-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.ImageField(upload_to=''),
        ),
    ]
