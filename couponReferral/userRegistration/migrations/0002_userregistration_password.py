# Generated by Django 2.1.1 on 2020-01-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
    ]