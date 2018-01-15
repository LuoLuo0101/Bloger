# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-15 16:26
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_profile',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('app_name', models.CharField(max_length=100, verbose_name='权限名')),
                ('model_name', models.CharField(max_length=100, verbose_name='模型名')),
            ],
            options={
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
                'db_table': 'content_type',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=100, verbose_name='分组/角色名')),
            ],
            options={
                'verbose_name': '分组/角色表',
                'verbose_name_plural': '分组/角色表',
                'db_table': 'group',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('group_id', models.IntegerField(verbose_name='分组id')),
                ('permission_id', models.IntegerField(verbose_name='权限id')),
            ],
            options={
                'verbose_name': '分组/角色权限表',
                'verbose_name_plural': '分组/角色权限表',
                'db_table': 'group_permission',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=100, verbose_name='权限名')),
                ('content_type_id', models.IntegerField(verbose_name='内容类型id')),
            ],
            options={
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
                'db_table': 'permission',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserExtendInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(unique=True, verbose_name='用户id')),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.IntegerField(choices=[(1, '男'), (0, '女'), (2, '未知')], default=2)),
                ('desc', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='个人描述')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='住址')),
                ('mobile', models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='电话')),
                ('focus', models.IntegerField(default=0, verbose_name='关注人数')),
                ('refocus', models.IntegerField(default=0, verbose_name='被关注人数')),
                ('integral', models.IntegerField(default=0, verbose_name='积分')),
                ('image', models.ImageField(default='image/user/default.jpg', max_length=200, upload_to='image/user', verbose_name='个人头像')),
            ],
            options={
                'verbose_name': '用户信息扩展表',
                'verbose_name_plural': '用户信息扩展表',
                'db_table': 'user_info',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('group_id', models.IntegerField(verbose_name='分组id')),
            ],
            options={
                'verbose_name': '用户分组/角色表',
                'verbose_name_plural': '用户分组/角色表',
                'db_table': 'user_group',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('permission_id', models.IntegerField(verbose_name='权限id')),
            ],
            options={
                'verbose_name': '用户权限表',
                'verbose_name_plural': '用户权限表',
                'db_table': 'user_permission',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='contenttype',
            unique_together=set([('app_name', 'model_name')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
