# Generated by Django 2.1.7 on 2019-04-01 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0010_auto_20190401_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='recipe_name',
        ),
    ]
