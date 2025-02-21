# Generated by Django 5.0.3 on 2024-03-15 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_detail", "0004_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="Address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="user_detail.address",
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="Contact",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="user_detail.contact",
            ),
        ),
    ]
