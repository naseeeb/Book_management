# Generated by Django 3.1.2 on 2024-05-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_databaseconfiguration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseconfiguration',
            name='port',
            field=models.IntegerField(null=True),
        ),
    ]