# Generated by Django 4.0.4 on 2022-11-06 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="modelblog",
            options={"verbose_name_plural": "Articulos"},
        ),
    ]