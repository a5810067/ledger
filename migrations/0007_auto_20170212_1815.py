# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_note_cost_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='cost_total',
        ),
        migrations.AddField(
            model_name='total',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.Note'),
        ),
    ]
