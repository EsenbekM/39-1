# Generated by Django 5.0.4 on 2024-04-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="test",
            field=models.IntegerField(null=True),
        ),
    ]
