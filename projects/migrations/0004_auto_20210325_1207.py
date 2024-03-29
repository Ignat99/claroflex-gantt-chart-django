# Generated by Django 3.1.5 on 2021-03-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttask',
            name='actual_close_date',
            field=models.DateField(blank=True, null=True, verbose_name='Actual close date'),
        ),
        migrations.AddField(
            model_name='projecttask',
            name='actual_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Actual start date'),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='close_date',
            field=models.DateField(verbose_name='Close date by plan'),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='start_date',
            field=models.DateField(verbose_name='Start date  by plan'),
        ),
    ]
