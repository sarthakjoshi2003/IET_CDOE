# Generated by Django 4.0.4 on 2022-06-26 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_delete_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course_details',
            new_name='Course_Detail',
        ),
        migrations.RenameModel(
            old_name='useful_links',
            new_name='Useful_Link',
        ),
    ]
