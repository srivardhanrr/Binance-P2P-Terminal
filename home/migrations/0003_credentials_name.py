# Generated by Django 4.0.4 on 2022-10-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_credentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='name',
            field=models.CharField(default='User', max_length=255),
        ),
    ]