# Generated by Django 3.0.7 on 2020-07-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicuha', '0002_movieinfo_ending_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seance',
            name='begin_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seance',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]