# Generated by Django 3.2 on 2021-04-15 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='max_players',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
