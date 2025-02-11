# Generated by Django 4.2.16 on 2024-11-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fog', '0008_game_is_alpha_alter_game_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
