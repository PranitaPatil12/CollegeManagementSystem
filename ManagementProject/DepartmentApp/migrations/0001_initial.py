# Generated by Django 4.0 on 2022-01-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Department_name', models.CharField(max_length=100, unique=True)),
                ('Intake', models.IntegerField()),
            ],
        ),
    ]