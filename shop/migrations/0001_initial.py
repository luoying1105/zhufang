# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 15:28
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
            name='Administrative_division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='行政区域')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='装修质量')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Layouts',
                'ordering': ('name',),
                'verbose_name': 'layout',
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.CharField(default='宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'cumpies',
                'ordering': ('name',),
                'verbose_name': 'cumpus',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='城市')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'cities',
                'ordering': ('name',),
                'verbose_name': 'city',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'devices',
                'ordering': ('name',),
                'verbose_name': 'device',
            },
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedroom_count', models.IntegerField(default=1)),
                ('bashroom_count', models.IntegerField(default=1)),
                ('livingroom_count', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(db_index=True, max_length=200, verbose_name='与校区距离')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='商品名')),
                ('slug', models.SlugField(max_length=200, verbose_name='链接地址')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='商品图像')),
                ('orientations', models.CharField(default='朝南', max_length=20, verbose_name='房间朝向')),
                ('height', models.IntegerField(default=0, verbose_name='房间层高')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('stock', models.PositiveIntegerField(verbose_name='库存')),
                ('available', models.BooleanField(default=True, verbose_name='是否上架')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('apartment_layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='shop.ApartmentLayout')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_posts', to=settings.AUTH_USER_MODEL)),
                ('campus', models.ManyToManyField(related_name='campus_locate', to='shop.Campus')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category')),
                ('device', models.ManyToManyField(related_name='device', to='shop.Device')),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='huxing', to='shop.Layout')),
                ('locate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_locate', to='shop.City')),
                ('locations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lactional', to='shop.Administrative_division')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Updown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='小区名称')),
                ('address', models.CharField(db_index=True, max_length=300, verbose_name='详细地址')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'cities',
                'ordering': ('name',),
                'verbose_name': '',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='updown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updown_locate', to='shop.Updown'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
