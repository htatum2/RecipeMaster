# Generated by Django 2.1.5 on 2019-04-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0020_auto_20190408_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='food_default.jpg', upload_to='recipe_pics'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image2',
            field=models.ImageField(blank=True, default='food_default.jpg', upload_to='recipe_pics'),
        ),
    ]
