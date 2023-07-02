# Generated by Django 4.2.2 on 2023-06-28 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop_projects", "0005_auto_20230628_0949"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="shop_projects.category"
            ),
        ),
    ]
