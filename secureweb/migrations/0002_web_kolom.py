# Generated by Django 2.2.12 on 2021-02-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='kolom',
            field=models.IntegerField(null=True),
        ),
    ]