# Generated by Django 4.2.2 on 2023-07-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_projects', '0015_creator_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='donat',
            name='status',
            field=models.IntegerField(choices=[(0, 'Archived'), (1, 'Available')], default=1),
        ),
    ]
