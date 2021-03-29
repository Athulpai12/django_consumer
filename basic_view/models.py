from django.db import models

# Create your models here.
from basic_view import utils, consumer


class UserEmail(models.Model):

    email = models.EmailField(max_length=254)


class UserData(models.Model):

    user_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(null=True, max_length=255)
    email = models.ManyToManyField(to=UserEmail)
    action_result = models.BooleanField(default=False)
    interview_transcription = models.CharField(max_length=255)
    move_forward = models.BooleanField()
    appointment_date = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.move_forward:
            try:
                utils.send_email(self.email)
                self.action_result = True
                consumer.WebsocketConsumer.send(serializers.serialize(['json', models_obj]))
            except Exception:
                pass