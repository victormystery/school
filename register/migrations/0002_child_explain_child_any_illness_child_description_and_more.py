# Generated by Django 4.0.4 on 2022-05-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='Explain',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='child',
            name='any_illness',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='child',
            name='doctor_consultation',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='email_father',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='email_mother',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='father',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='hearing_difficulty',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='image',
            field=models.ImageField(height_field=50, null=True, upload_to='passport/', width_field=80),
        ),
        migrations.AddField(
            model_name='child',
            name='immunized',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='medical_certificate',
            field=models.ImageField(null=True, upload_to='certify/'),
        ),
        migrations.AddField(
            model_name='child',
            name='mobile_father',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='mobile_mother',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='mother',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='occupation_father',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='occupation_mother',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='spectacles',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='vision',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='Previous_class',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='Previous_school',
            field=models.TextField(blank=True),
        ),
    ]