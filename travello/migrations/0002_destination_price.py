# Generated by Django 3.0.8 on 2020-07-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
