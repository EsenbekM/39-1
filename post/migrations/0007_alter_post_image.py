# Generated by Django 5.0.4 on 2024-04-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0006_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="meme/"),
        ),
    ]