# Generated by Django 2.2.19 on 2022-12-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='tag',
            field=models.CharField(blank=True, max_length=64, verbose_name='Filter Tag'),
        ),
    ]