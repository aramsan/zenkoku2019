# Generated by Django 2.1.7 on 2019-05-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0008_auto_20190503_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
