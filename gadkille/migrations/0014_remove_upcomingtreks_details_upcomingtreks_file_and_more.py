# Generated by Django 4.0.4 on 2022-09-02 19:29

from django.db import migrations, models
import django.utils.timezone
import gadkille.models


class Migration(migrations.Migration):

    dependencies = [
        ('gadkille', '0013_trekphoto_delete_contactdetail_remove_gallery_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingtreks',
            name='details',
        ),
        migrations.AddField(
            model_name='upcomingtreks',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='gadkille/images/', validators=[gadkille.models.ValidateSize.validate_1MB]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upcomingtreks',
            name='image',
            field=models.ImageField(upload_to='gadkille/images/', validators=[gadkille.models.ValidateSize.validate_1MB]),
        ),
    ]
