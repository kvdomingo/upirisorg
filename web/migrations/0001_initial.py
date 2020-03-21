# Generated by Django 3.0.4 on 2020-03-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('personal_email', models.EmailField(max_length=254)),
                ('up_email', models.EmailField(max_length=254)),
                ('contact_number', models.BigIntegerField()),
                ('college', models.CharField(max_length=256)),
                ('year', models.SmallIntegerField()),
                ('course', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
            ],
        ),
    ]
