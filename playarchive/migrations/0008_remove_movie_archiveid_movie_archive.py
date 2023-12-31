# Generated by Django 4.2.2 on 2023-10-16 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("playarchive", "0007_remove_movie_archive_movie_archiveid"),
    ]

    operations = [
        migrations.RemoveField(model_name="movie", name="archiveid",),
        migrations.AddField(
            model_name="movie",
            name="archive",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="movies",
                to="playarchive.archive",
            ),
            preserve_default=False,
        ),
    ]
