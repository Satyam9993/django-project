# Generated by Django 4.1.7 on 2023-03-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='dummy', max_length=200),
            preserve_default=False,
        ),
    ]
