# Generated by Django 3.1 on 2020-08-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workmateapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dogg',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]