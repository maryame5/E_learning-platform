# Generated by Django 5.1.1 on 2024-12-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("e_learning", "0017_admin_profil_img_teacher_profil_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="profil_img",
            field=models.ImageField(
                blank=True,
                default="images/default_profile.png",
                null=True,
                upload_to="img_profile/",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="profil_img",
            field=models.ImageField(
                blank=True,
                default="images/default_profile.png",
                null=True,
                upload_to="img_profile/",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="profil_img",
            field=models.ImageField(
                blank=True,
                default="images/default_profile.png",
                null=True,
                upload_to="img_profile/",
            ),
        ),
    ]
