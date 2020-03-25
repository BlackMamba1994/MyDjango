# Generated by Django 3.0.3 on 2020-03-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='image',
            field=models.ImageField(default='', upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='newsgame',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='oldgames',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='oldgames',
            name='image2',
            field=models.ImageField(blank='True', null='True', upload_to='media/', verbose_name='Изображение1'),
        ),
        migrations.AlterField(
            model_name='oldgames',
            name='image3',
            field=models.ImageField(blank='True', null='True', upload_to='media/', verbose_name='Изображение2'),
        ),
    ]
