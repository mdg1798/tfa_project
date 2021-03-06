# Generated by Django 2.2.7 on 2019-12-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0003_auto_20191202_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_twitches',
            field=models.BooleanField(),
        ),
    ]
