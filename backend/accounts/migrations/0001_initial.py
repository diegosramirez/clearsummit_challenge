# Generated by Django 2.0.4 on 2019-11-21 16:49

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import helpers.utils
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0009_alter_user_last_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=32, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        default=None,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=128,
                        null=True,
                        verbose_name="password",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=32,
                        null=True,
                        verbose_name="First Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=32,
                        null=True,
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "app_data",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "stripe_id",
                    models.CharField(
                        blank=True, default=None, max_length=256, null=True
                    ),
                ),
                (
                    "authy_id",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=32,
                        null=True,
                        verbose_name="authy_id",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default=None, max_length=128, null=True, region=None
                    ),
                ),
                (
                    "failed_tfa_attempts",
                    models.SmallIntegerField(
                        blank=True, default=0, verbose_name="failed_tfa_count"
                    ),
                ),
                ("disabled", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="PasswordReset",
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
                ("token", models.CharField(max_length=256)),
                (
                    "expires_at",
                    models.DateTimeField(default=helpers.utils.week_expiration_period),
                ),
                ("used", models.BooleanField(default=False)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
