# Generated by Django 3.2.6 on 2021-08-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210809_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ManyToManyField(to='api.Category'),
        ),
    ]
