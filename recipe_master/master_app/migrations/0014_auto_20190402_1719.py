# Generated by Django 2.1.7 on 2019-04-02 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0013_auto_20190402_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipereview',
            old_name='overallRating',
            new_name='rating',
        ),
    ]
