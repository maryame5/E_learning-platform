# Generated by Django 5.1.1 on 2024-12-15 10:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("e_learning", "0014_alter_comments_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comments",
            options={"ordering": ["-created_at"]},
        ),
    ]
