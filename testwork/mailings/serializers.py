from rest_framework import serializers

from .models import Client, Mailing, MessageLog


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'number', 'code', 'tag', 'time_zone'
        )
        model = Client

    def validate_number(self, phone_number):
        if str(phone_number)[0] != '7':
            raise serializers.ValidationError(
                'Введите номер в формате 7XXXXXXXXXX'
            )
        return phone_number


class MessageLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'send_time', 'status', 'mailing', 'client'
        )
        model = MessageLog


class MailinglistSerializer(serializers.ModelSerializer):
    send_messages = serializers.SerializerMethodField()
    not_send_messages = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id', 'start_time', 'finish_time',
            'text', 'tag', 'code', 'send_messages', 'not_send_messages'
        )
        model = Mailing

    def get_send_messages(self, obj):
        return obj.messages.filter(status='S').count()

    def get_not_send_messages(self, obj):
        return obj.messages.filter(status='N').count()


class MailingSerializer(serializers.ModelSerializer):
    messages = MessageLogSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'id', 'start_send_time', 'end_send_time',
            'text', 'tag', 'code', 'messages'
        )
        model = Mailing
        