# Generated by Django 3.0.7 on 2020-07-03 15:03

from django.db import migrations
from django.contrib.postgres.operations import UnaccentExtension


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0001_initial'),
    ]

    operations = [
        UnaccentExtension()
    ]