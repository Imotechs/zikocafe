# Generated by Django 4.0.1 on 2022-03-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0008_remove_phone_key_remove_programmers_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='customer',
            field=models.CharField(default='Admin', max_length=200),
        ),
    ]