# Generated by Django 4.0.4 on 2022-08-27 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gadkille', '0008_rename_contact_contactdetail_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='CustomerContact',
        ),
        migrations.AlterModelOptions(
            name='customercontact',
            options={'verbose_name': 'Customer Contact', 'verbose_name_plural': 'Customer Contact'},
        ),
    ]
