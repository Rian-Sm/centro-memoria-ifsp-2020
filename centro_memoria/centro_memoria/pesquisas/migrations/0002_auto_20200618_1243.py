# Generated by Django 3.0.7 on 2020-06-18 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membro',
            old_name='image',
            new_name='imagem',
        ),
    ]