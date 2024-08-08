# Generated by Django 5.0.8 on 2024-08-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='player',
        ),
        migrations.AddField(
            model_name='score',
            name='player_id',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='player_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
