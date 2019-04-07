# Generated by Django 2.1.2 on 2019-04-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0017_review_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients_list',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='', max_length=2000),
        ),
    ]