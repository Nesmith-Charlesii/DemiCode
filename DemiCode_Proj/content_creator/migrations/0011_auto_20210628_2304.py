# Generated by Django 3.1.7 on 2021-06-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0010_auto_20210626_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creative',
            name='confirmPW',
            field=models.CharField(max_length=150),
        ),
    ]
