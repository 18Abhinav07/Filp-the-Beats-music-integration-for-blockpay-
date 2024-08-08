# Generated by Django 5.0.8 on 2024-08-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_score_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='score',
            name='sequence',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='score',
            name='player_id',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('player_id', 'sequence')},
        ),
    ]
