# Generated by Django 5.1.1 on 2024-12-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("e_learning", "0015_alter_comments_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="profil_img",
            field=models.ImageField(blank=True, null=True, upload_to="img_profile/"),
        ),
    ]
