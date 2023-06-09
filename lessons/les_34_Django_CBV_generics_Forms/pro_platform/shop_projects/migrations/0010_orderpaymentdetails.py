# Generated by Django 4.2.2 on 2023-07-03 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop_projects", "0009_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderPaymentDetails",
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
                ("payed_at", models.DateTimeField(blank=True, null=True)),
                ("card_ends_with", models.CharField(blank=True, max_length=5)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Pending"), (1, "Confirmed")], default=0
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_details",
                        to="shop_projects.order",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Order Payment Details",
            },
        ),
    ]
