# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20180315_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='creator_username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='owner_username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
