# Generated by Django 4.0.5 on 2022-06-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_alter_tablecat_options_remove_sotr_rank_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotr',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='sotr',
            name='surname',
        ),
        migrations.AlterField(
            model_name='sotr',
            name='education',
            field=models.CharField(blank=True, max_length=100, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='sotr',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Ф.И.О.'),
        ),
    ]