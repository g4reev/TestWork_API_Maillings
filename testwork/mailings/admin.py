from django.contrib import admin

from .models import Client, Mailing, MessageLog

admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(MessageLog)