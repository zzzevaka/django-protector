# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 15:25
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
        ('protector', '0006_auto_20180726_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryGenericUserToGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.IntegerField(blank=True, null=True, verbose_name='roles')),
                ('group_id', models.PositiveIntegerField(verbose_name='group id')),
                ('reason', models.TextField(validators=[django.core.validators.MinLengthValidator(1)], verbose_name='change reason')),
                ('changed_at', models.DateTimeField(auto_now_add=True, verbose_name='change date')),
                ('group_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='group content type')),
                ('initiator', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='history_generic_group_initiator',
                    to=settings.AUTH_USER_MODEL
                )),
                ('responsible', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='history_created_group_relations',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='responsible'
                )),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='history_generic_group_relations',
                    to=settings.AUTH_USER_MODEL
                )),
            ],
            options={
                'verbose_name': 'generic user to group history',
                'verbose_name_plural': 'generic user to group histories',
                'permissions': (('view_generic_group_history', 'view generic group history'),),
            },
        ),
        migrations.CreateModel(
            name='HistoryOwnerToPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True, verbose_name='object id')),
                ('owner_object_id', models.PositiveIntegerField(verbose_name='owner id')),
                ('roles', models.IntegerField(default=1, verbose_name='roles')),
                ('reason', models.TextField(validators=[django.core.validators.MinLengthValidator(1)], verbose_name='change reason')),
                ('changed_at', models.DateTimeField(auto_now_add=True, verbose_name='change date')),
                ('content_type', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='history_restriction_group_relations',
                    to='contenttypes.ContentType',
                    verbose_name='object type',
                )),
                ('initiator', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='history_owner_to_perm_initiator',
                    to=settings.AUTH_USER_MODEL
                )),
                ('owner_content_type',models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='history_restricted_object_relations',
                    to='contenttypes.ContentType',
                    verbose_name='owner type'
                )),
                ('permission', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='history_generic_restriction_relations',
                    to='auth.Permission',
                    verbose_name='permission'
                )),
                ('responsible', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='history_created_permission_relations',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='responsible'
                )),
            ],
            options={
                'verbose_name': 'owner to permission history',
                'verbose_name_plural': 'owner to permission histories',
                'permissions': (('view_owner_to_perm_history', 'view owner to permission history'),),
            },
        ),
    ]
