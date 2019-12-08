# Generated by Django 2.2.7 on 2019-12-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Latitude',
            field=models.FloatField(help_text='Enter the Latitude'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(choices=[('Ground_Plane', 'Ground_Plane'), ('Above_Ground', 'Above_Ground'), ('Other', 'Other')], default='Other', help_text='Locations of the squirrel', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Longitude',
            field=models.FloatField(help_text='Enter the Longitude'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_from',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], help_text='Runs or not', max_length=5),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='Unique ID of squirrel', max_length=100),
        ),
    ]