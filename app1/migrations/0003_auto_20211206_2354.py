# Generated by Django 3.2.9 on 2021-12-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211206_1919'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tokens',
        ),
        migrations.AddField(
            model_name='userdata',
            name='counter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='pos',
            field=models.IntegerField(null=True),
        ),
    ]
