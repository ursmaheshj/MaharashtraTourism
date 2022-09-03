# Generated by Django 4.0.4 on 2022-09-03 08:50

from django.db import migrations, models
import gadkille.models


class Migration(migrations.Migration):

    dependencies = [
        ('gadkille', '0014_remove_upcomingtreks_details_upcomingtreks_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingtreks',
            name='file',
            field=models.FileField(upload_to='gadkille/images/', validators=[gadkille.models.ValidateSize.validate_2MB]),
        ),
    ]
