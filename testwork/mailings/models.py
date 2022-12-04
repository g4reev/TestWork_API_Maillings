from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


STATUS_CHOICES = (
        ('Message sent', 'send'),
        ('Message not sent', 'not send'),
    )


class Client(models.Model):
    number = models.BigIntegerField(
        'Phone number',
        unique=True,
        validators=[
            MaxValueValidator(79999999999),
            MinValueValidator(70000000000)
        ]
    )
    code = models.CharField('Phone provider code', max_length=8)
    tag = models.CharField('Tag', null=True, blank=True, max_length=64)
    time_zone = models.CharField('TimeZone', max_length=24)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return str(self.number)


class Mailing(models.Model):
    start_time = models.DateTimeField(
        'Date and time of the start of the mailing'
        )
    text = models.TextField('mailing text')
    code = models.CharField('Filter phone code', max_length=8)
    tag = models.CharField('Filter Tag', blank=True, max_length=64)
    finish_time = models.DateTimeField(
        'Date and time of the finish of the mailing'
    )

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return str(self.text)


class MessageLog(models.Model):
    send_time = models.DateTimeField('Send data & time', auto_now_add=True)
    status = models.CharField(
        'Send status', max_length=24,
        choices=STATUS_CHOICES
        )
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE,
        related_name='message', verbose_name='Mailing'
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        related_name='messages', verbose_name='client'
    )

    class Meta:
        ordering = ['-send_time']

    def __str__(self) -> str:
        return str(self.send_time)
