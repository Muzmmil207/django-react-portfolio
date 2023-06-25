# Generated by Django 4.1.7 on 2023-06-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plugins", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metatext",
            name="active",
            field=models.BooleanField(
                default=True,
                help_text="If False, it will return empty Response",
                verbose_name="Active",
            ),
        ),
        migrations.AlterField(
            model_name="metatext",
            name="key",
            field=models.CharField(
                help_text="It will be using to make a queryset",
                max_length=255,
                unique=True,
                verbose_name="Key",
            ),
        ),
        migrations.AlterField(
            model_name="metatext",
            name="name",
            field=models.CharField(default="", max_length=100, verbose_name="Name"),
        ),
    ]