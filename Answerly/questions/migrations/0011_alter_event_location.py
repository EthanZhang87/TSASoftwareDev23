# Generated by Django 4.2.3 on 2023-10-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_remove_eventresponse_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='America', max_length=200),
        ),
    ]