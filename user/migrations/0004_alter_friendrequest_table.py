# Generated by Django 4.1.6 on 2023-04-27 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_friendrequest'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='friendrequest',
            table='friend_requests',
        ),
    ]