# Generated by Django 4.2.2 on 2023-07-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_projects', '0010_orderpaymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
