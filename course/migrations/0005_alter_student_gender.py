# Generated by Django 3.2.4 on 2021-06-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=7),
        ),
    ]