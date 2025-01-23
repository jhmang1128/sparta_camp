# Generated by Django 4.2 on 2025-01-23 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="writer",
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
