# Generated by Django 4.0.2 on 2022-03-09 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='eze ayo azaki(Default)', max_length=200, null=True)),
                ('title', models.CharField(default='', max_length=200, null=True)),
                ('desc', models.CharField(default=('',), max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]