# Generated by Django 4.0.4 on 2022-05-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_faculty_faculty_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='logo',
            field=models.ImageField(default='images/index/cdoe1.png', upload_to='images/index/'),
        ),
    ]
