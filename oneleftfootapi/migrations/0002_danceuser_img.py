# Generated by Django 3.2.4 on 2021-06-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneleftfootapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='danceuser',
            name='img',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
