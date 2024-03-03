# Generated by Django 5.0.2 on 2024-02-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='max_count',
            field=models.IntegerField(default=0, verbose_name='Максимальное количество студентов в группе'),
        ),
        migrations.AddField(
            model_name='product',
            name='min_count',
            field=models.IntegerField(default=0, verbose_name='Минимальное количество студентов в группе'),
        ),
        migrations.AlterField(
            model_name='access',
            name='value',
            field=models.BooleanField(default=False, verbose_name='Доступ к курсу'),
        ),
    ]