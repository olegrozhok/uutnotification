# Generated by Django 4.2.1 on 2023-06-07 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uutpost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='mobile',
            new_name='mobile_addr',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='name',
            new_name='name_addr',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='tg',
            new_name='tg_addr',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='vk',
            new_name='vk_addr',
        ),
    ]