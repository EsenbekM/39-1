# Generated by Django 5.0.4 on 2024-04-12 12:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_post_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="test",
        ),
    ]
