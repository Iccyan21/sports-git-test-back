# Generated by Django 4.2.2 on 2023-10-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playarchive", "0005_alter_movie_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archive",
            name="archiveid",
            field=models.AutoField(
                primary_key=True, serialize=False, unique=True, verbose_name="ArchiveID"
            ),
        ),
    ]
