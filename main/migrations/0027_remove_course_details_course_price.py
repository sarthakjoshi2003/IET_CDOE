# Generated by Django 4.0.4 on 2022-06-26 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_course_details_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_details',
            name='course_price',
        ),
    ]