# Generated by Django 3.2.4 on 2021-06-09 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='DanceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='oneleftfootapi.danceuser')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='oneleftfootapi.danceuser')),
            ],
        ),
        migrations.CreateModel(
            name='DanceTypeJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=8)),
                ('dance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.dancetype')),
                ('dance_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.danceuser')),
                ('skill_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.skilllevel')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dance_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.danceuser')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.day')),
            ],
        ),
    ]