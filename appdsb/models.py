from django.core.mail import send_mail
from django.db import models
import telepot
from django.views.generic import TemplateView


# Create your models here.


class DSB(models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.temp)

    #  Envoyer Mail et telegram
    def save(self, *args, **kwargs):
        # site==https://api.telegram.org/bot5855381429:AAGB66z5kub63McgS--szI4g0kquGOi8j7M/getUpdates
        token = '5855381429:AAGB66z5kub63McgS--szI4g0kquGOi8j7M'
        rece_id = 5157060096
        bot = telepot.Bot(token)
        if self.temp > 10 or self.temp < 0:
            print(bot.sendMessage(rece_id, 'température sévère,' + str(self.temp)))
            send_mail(
                'température sévère,' + str(self.temp),
                'anomalie dans la machine,' + str(self.dt),
                'mouad.elallali@ump.ac.ma',
                ['mouad.elallali@ump.ac.ma'],
                fail_silently=False
            )
        if 0 <= self.temp <= 2 or 8 <= self.temp <= 10:
            print(bot.sendMessage(rece_id, 'température critique,' + str(self.temp)))
            send_mail(
                'température critique,' + str(self.temp),
                'anomalie dans la machine,' + str(self.dt),
                'mouad.elallali@ump.ac.ma',
                ['mouad.elallali@ump.ac.ma'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)




