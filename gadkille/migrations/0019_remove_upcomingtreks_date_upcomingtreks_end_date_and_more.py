# Generated by Django 4.0.4 on 2022-09-04 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gadkille', '0018_alter_upcomingtreks_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingtreks',
            name='date',
        ),
        migrations.AddField(
            model_name='upcomingtreks',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upcomingtreks',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
