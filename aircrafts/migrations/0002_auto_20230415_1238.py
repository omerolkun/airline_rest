# Generated by Django 3.2.12 on 2023-04-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircrafts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraft',
            old_name='aircraft_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='type',
            field=models.CharField(db_column='aircraft_type', max_length=25),
        ),
    ]
