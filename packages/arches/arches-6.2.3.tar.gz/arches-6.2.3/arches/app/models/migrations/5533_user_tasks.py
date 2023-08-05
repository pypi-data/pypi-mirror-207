# Generated by Django 2.2.6 on 2019-11-12 13:07

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("models", "5473_move_exportable_to_node"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserXTask",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ("taskid", models.UUIDField(blank=True, null=True, serialize=False)),
                ("status", models.TextField(null=True, default="PENDING")),
                ("date_start", models.DateTimeField(blank=True, null=True)),
                ("date_done", models.DateTimeField(blank=True, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "user_x_tasks", "managed": True,},
        ),
    ]
