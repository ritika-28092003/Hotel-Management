# Generated by Django 4.2.3 on 2023-07-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_room_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_days',
            field=models.IntegerField(null=True),
        ),
    ]
