# Generated by Django 4.2.2 on 2023-06-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_projects", "0008_project_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="other_contributors",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="url",
            field=models.CharField(max_length=150, null=True),
        ),
    ]