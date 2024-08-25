# Generated by Django 5.0.8 on 2024-08-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                (
                    "name",
                    models.CharField(help_text="name of the movie", max_length=200),
                ),
                (
                    "duration",
                    models.FloatField(
                        blank=True, default=0.0, help_text="in minutes", null=True
                    ),
                ),
                (
                    "rating",
                    models.FloatField(
                        blank=True, default=0.0, help_text="out of 10", null=True
                    ),
                ),
            ],
        ),
    ]
