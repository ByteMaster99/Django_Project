# Generated by Django 5.0.3 on 2024-03-14 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_detail", "0002_vendor"),
    ]

    operations = [
        migrations.CreateModel(
            name="address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Line_1", models.CharField(max_length=300)),
                ("Line_2", models.CharField(max_length=300)),
                ("Pincode", models.CharField(max_length=300)),
                ("State", models.CharField(max_length=300)),
                ("District", models.CharField(max_length=300)),
                ("City", models.CharField(max_length=300)),
                ("created_by", models.IntegerField()),
                ("created_date", models.DateField(default=datetime.datetime.now)),
                ("updated_by", models.IntegerField()),
                ("updated_date", models.DateField(default=datetime.datetime.now)),
                ("status", models.SmallIntegerField(default=1)),
            ],
        ),
    ]
