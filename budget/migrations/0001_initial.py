# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('ExpenditureSk', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(verbose_name=b'Expenditure Date')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=14, verbose_name=b'Expenditure Amount')),
                ('For', models.CharField(max_length=100, verbose_name=b'Expenditure For')),
            ],
            options={
                'db_table': 'Expendiutre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('ExpenseTypeSk', models.AutoField(primary_key=True, serialize=False)),
                ('ExpenseTypeName', models.CharField(max_length=100, verbose_name=b'Expense Type')),
            ],
            options={
                'db_table': 'ExpenseType',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='expenditure',
            name='ExpenseTypeTags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Expense', to='budget.ExpenseType'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='UserId',
            field=models.ForeignKey(db_column=b'UserId', on_delete=django.db.models.deletion.CASCADE, related_name='Expense', to=settings.AUTH_USER_MODEL),
        ),
    ]
