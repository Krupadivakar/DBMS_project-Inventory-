# Generated by Django 3.1.3 on 2020-12-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=25)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=25)),
            ],
        ),
    ]
