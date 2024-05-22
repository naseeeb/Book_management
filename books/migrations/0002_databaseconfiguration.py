# Generated by Django 3.1.2 on 2024-05-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]