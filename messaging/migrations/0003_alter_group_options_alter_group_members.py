# Generated by Django 5.0.6 on 2024-07-18 13:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="group",
            options={
                "verbose_name": "Chat Group",
                "verbose_name_plural": "Chat Groups",
            },
        ),
        migrations.AlterField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="groups_members", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]