# Generated by Django 3.0.7 on 2020-07-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicuha', '0010_auto_20200704_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='hall_name',
            field=models.CharField(max_length=20),
        ),
    ]
