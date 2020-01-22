# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-30 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsulAlerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulalert_type', models.CharField(choices=[('InfluxDB', 'InfluxDB'), ('Slack', 'Slack'), ('Mattermost', 'Mattermost'), ('PagerDuty', 'PagerDuty'), ('HipChat', 'HipChat'), ('OpsGenie', 'OpsGenie'), ('AWS-SNS', 'AWS-SNS'), ('VictorOps', 'VictorOps')], default='PagerDuty', max_length=20, verbose_name='Service Name')),
                ('attributes', freenasUI.freeadmin.models.fields.DictField(editable=False, verbose_name='Attributes')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Consul Alerts',
                'ordering': ['consulalert_type'],
            },
        ),
   ]