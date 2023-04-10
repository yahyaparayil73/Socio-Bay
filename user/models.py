from django.db import models

# Create your models here.


class User(models.Model):

    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to = 'user/',default='')
    user_aboutof = models.CharField(max_length=200,default='None', blank=True, null=True)
    user_status = models.IntegerField(default=1, blank=True, null=True)
    user_last_seen = models.DateTimeField(default=None, blank=True, null=True)
    user_online_status = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'users'


class Chat(models.Model):

    chat_status = models.IntegerField(default=None, blank=True, null=True)
    chat_sender_id = models.IntegerField()
    chat_reciever_id = models.IntegerField()
    chat_start_date = models.DateTimeField(default=None, blank=True, null=True)
    chat_last_update = models.DateTimeField(default=None, blank=True, null=True)
    chat_unread_count = models.IntegerField(default=0, blank=True, null=True)
    chat_last_message_sender = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'chat'




class Message(models.Model):

    message_text = models.TextField(default=None, blank=False, null=False)
    message_sender_id = models.IntegerField()
    message_timestamp = models.DateTimeField(default=None, blank=True, null=True)
    message_status = models.IntegerField(default=None, blank=True, null=True)
    message_chat_id = models.IntegerField(default=None, blank=False, null=False)

    class Meta:
        db_table = 'message'


class Complaint(models.Model):

    complaint_sub = models.CharField(max_length = 300)
    complaint_body = models.CharField(max_length = 300)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'complaints'

class FriendRequest(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, default='pending')

    class Meta:
        db_table = 'friend requests'

    