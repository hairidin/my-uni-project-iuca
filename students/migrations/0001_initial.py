# Generated by Django 2.2.11 on 2020-03-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
            ],
        ),
    ]