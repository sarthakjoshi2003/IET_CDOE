# Generated by Django 4.0.4 on 2022-05-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_student_course_enrolling_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='about_faculty',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus fuga\n                                            ratione molestiae unde provident quibusdam sunt, doloremque. Error omnis\n                                            mollitia, ex dolor sequi. Et, quibusdam excepturi. Animi assumenda,\n                                            consequuntur dolorum odio sit inventore aliquid, optio fugiat alias.\n                                            Veritatis minima, dicta quam repudiandae repellat non sit, distinctio,\n                                            impedit, expedita tempora numquam?', max_length=300),
        ),
    ]
