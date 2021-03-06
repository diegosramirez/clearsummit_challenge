# Generated by Django 2.0.4 on 2019-08-08 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import helpers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("put_key", models.TextField(default=None, null=True)),
                (
                    "aws_file",
                    models.FileField(
                        default=None,
                        max_length=180,
                        null=True,
                        upload_to=helpers.models.user_based_path,
                    ),
                ),
                ("name", models.CharField(default=None, max_length=120, null=True)),
                ("soft_deleted", models.BooleanField(default=False)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
