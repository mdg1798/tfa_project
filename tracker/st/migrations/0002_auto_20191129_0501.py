# Generated by Django 2.2.7 on 2019-11-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Incidence',
        ),
    ]
