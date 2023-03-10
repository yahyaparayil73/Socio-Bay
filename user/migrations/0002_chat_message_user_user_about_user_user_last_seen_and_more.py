# Generated by Django 4.1.6 on 2023-02-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_status', models.IntegerField(blank=True, default=None, null=True)),
                ('chat_sender_id', models.IntegerField()),
                ('chat_reciever_id', models.IntegerField()),
                ('chat_start_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('chat_last_update', models.DateTimeField(blank=True, default=None, null=True)),
                ('chat_unread_count', models.IntegerField(blank=True, default=0, null=True)),
                ('chat_last_message_sender', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(default=None)),
                ('message_sender_id', models.IntegerField()),
                ('message_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('message_status', models.IntegerField(blank=True, default=None, null=True)),
                ('message_chat_id', models.IntegerField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_about',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_last_seen',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_online_status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
