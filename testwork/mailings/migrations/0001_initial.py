# Generated by Django 2.2.19 on 2022-12-04 18:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(79999999999), django.core.validators.MinValueValidator(70000000000)], verbose_name='Phone number')),
                ('code', models.CharField(max_length=8, verbose_name='Phone provider code')),
                ('tag', models.CharField(blank=True, max_length=64, null=True, verbose_name='Tag')),
                ('time_zone', models.CharField(max_length=24, verbose_name='TimeZone')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Date and time of the start of the mailing')),
                ('text', models.TextField(verbose_name='mailing text')),
                ('code', models.CharField(max_length=8, verbose_name='Filter phone code')),
                ('tag', models.CharField(max_length=64, verbose_name='Filter Tag')),
                ('finish_time', models.DateTimeField(verbose_name='Date and time of the finish of the mailing')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='Send data & time')),
                ('status', models.CharField(choices=[('Message sent', 'send'), ('Message not sent', 'not send')], max_length=24, verbose_name='Send status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='mailings.Client', verbose_name='client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='mailings.Mailing', verbose_name='Mailing')),
            ],
            options={
                'ordering': ['-send_time'],
            },
        ),
    ]