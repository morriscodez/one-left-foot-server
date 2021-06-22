# Generated by Django 3.2.4 on 2021-06-22 15:36

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
                ('img', models.ImageField(upload_to='One-Left-Foot')),
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
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=8)),
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
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='oneleftfootapi.danceuser')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='oneleftfootapi.danceuser')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('dance_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.danceuser')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.day')),
            ],
            options={
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='oneleftfootapi.danceuser')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='oneleftfootapi.danceuser')),
            ],
            options={
                'unique_together': {('leader', 'follower')},
            },
        ),
        migrations.CreateModel(
            name='DanceTypeJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.dancetype')),
                ('dance_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.danceuser')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.role')),
                ('skill_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneleftfootapi.skilllevel')),
            ],
            options={
                'unique_together': {('dance_user', 'dance_type')},
            },
        ),
    ]
