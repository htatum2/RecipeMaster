# Generated by Django 2.1.5 on 2019-02-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0002_auto_20190213_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(default=0, verbose_name=1),
            preserve_default=False,
        ),
    ]
