# Generated by Django 4.1.6 on 2023-02-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_usuarios_rename_main_publicacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='is_instagram_admin',
            field=models.IntegerField(),
        ),
    ]
