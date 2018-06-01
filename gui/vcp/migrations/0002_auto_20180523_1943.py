# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-23 19:43
from __future__ import unicode_literals

from django.db import migrations, models


def populate_vcp_models(apps, schema_editor):
    vcenter_configuration_model = apps.get_model('vcp', 'vcenterconfiguration')
    if not vcenter_configuration_model.objects.all().count():
        vcenter_configuration_model.objects.create()


class Migration(migrations.Migration):

    dependencies = [
        ('vcp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcenterconfiguration',
            name='vc_installed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vcenterconfiguration',
            name='vc_password',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name=' vCenter Password'),
        ),
        migrations.AlterField(
            model_name='vcenterconfiguration',
            name='vc_username',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name=' vCenter Username'),
        ),
        migrations.RunPython(
            populate_vcp_models
        )
    ]