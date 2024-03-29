# Generated by Django 5.0.2 on 2024-02-28 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('owner', models.CharField(max_length=255, verbose_name='Автор')),
                ('start_time', models.DateTimeField(verbose_name='Время старта')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('link', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product', verbose_name='Продукт')),
                ('student', models.ManyToManyField(to='app.student', verbose_name='Студенты')),
            ],
            options={
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Продукт')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name_plural': 'Доступы к курсам',
            },
        ),
    ]
