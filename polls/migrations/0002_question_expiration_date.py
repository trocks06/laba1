# Generated by Django 5.1.2 on 2024-10-28 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 14, 45, 11, 48076, tzinfo=datetime.timezone.utc)),
        ),
    ]
