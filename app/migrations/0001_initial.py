# Generated by Django 3.0.5 on 2021-01-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
                ('empid', models.IntegerField()),
            ],
        ),
    ]
