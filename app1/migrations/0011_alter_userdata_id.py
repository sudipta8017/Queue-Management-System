# Generated by Django 4.0.1 on 2022-01-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_employee_counternumber_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
