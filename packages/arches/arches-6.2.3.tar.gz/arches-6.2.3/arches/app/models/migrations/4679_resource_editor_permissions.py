# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-25 11:36


import os
import uuid
import django.db.models.deletion
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.core import management
from arches.app.models.system_settings import settings


def add_permissions(apps, schema_editor, with_create_permissions=True):
    db_alias = schema_editor.connection.alias
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    write_nodegroup = Permission.objects.get(codename='write_nodegroup', content_type__app_label='models', content_type__model='nodegroup')
    delete_nodegroup = Permission.objects.get(codename='delete_nodegroup', content_type__app_label='models', content_type__model='nodegroup')

    resource_editor_group = Group.objects.using(db_alias).get(name='Resource Editor')
    resource_editor_group.permissions.add(write_nodegroup)
    resource_editor_group.permissions.add(delete_nodegroup)
    resource_editor_group = Group.objects.using(db_alias).get(name='Resource Reviewer')
    resource_editor_group.permissions.add(write_nodegroup)
    resource_editor_group.permissions.add(delete_nodegroup)
    resource_editor_group = Group.objects.using(db_alias).get(name='Crowdsource Editor')
    resource_editor_group.permissions.add(write_nodegroup)
    resource_editor_group.permissions.add(delete_nodegroup)


def remove_permissions(apps, schema_editor, with_create_permissions=True):
    db_alias = schema_editor.connection.alias
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    write_nodegroup = Permission.objects.get(codename='write_nodegroup', content_type__app_label='models', content_type__model='nodegroup')
    delete_nodegroup = Permission.objects.get(codename='delete_nodegroup', content_type__app_label='models', content_type__model='nodegroup')

    resource_editor_group = Group.objects.using(db_alias).get(name='Resource Editor')
    resource_editor_group.permissions.remove(write_nodegroup)
    resource_editor_group.permissions.remove(delete_nodegroup)
    resource_editor_group = Group.objects.using(db_alias).get(name='Resource Reviewer')
    resource_editor_group.permissions.remove(write_nodegroup)
    resource_editor_group.permissions.remove(delete_nodegroup)
    resource_editor_group = Group.objects.using(db_alias).get(name='Crowdsource Editor')
    resource_editor_group.permissions.remove(write_nodegroup)
    resource_editor_group.permissions.remove(delete_nodegroup)


class Migration(migrations.Migration):

    dependencies = [
        ('models', '4384_adds_rerender_widget_config'),
    ]

    operations = [
        ## the following command has to be run after the previous RunSQL commands that update the domain datatype values
        migrations.RunPython(add_permissions,remove_permissions),
    ]
