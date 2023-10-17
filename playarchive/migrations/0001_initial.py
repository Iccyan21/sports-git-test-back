# Generated by Django 4.2.2 on 2023-10-13 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Achive",
            fields=[
                (
                    "archiveid",
                    models.IntegerField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ArchiveID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("subtitle", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
            options={"verbose_name": "アーカイブ", "verbose_name_plural": "アーカイブ",},
        ),
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
                ("title", models.CharField(max_length=20)),
                ("video", models.FileField(upload_to="movies/")),
                (
                    "achive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to="playarchive.achive",
                    ),
                ),
            ],
        ),
    ]
