# Generated by Django 4.2.14 on 2024-07-13 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BookModel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(to="BookModel.author"),
        ),
    ]
